#!/usr/bin/env python3

import sys, random
import pandas as pd
from collections import OrderedDict
from shutil import copyfile
from person import Person
from people import People
from bucketlist import BucketList
from requestlist import RequestList

class Allocation(OrderedDict):

    def __str__(self):
        header = "Allocation (len=%d)\n" % len(self)
        return header + '\n'.join(map(str, self.items()))
    
    @staticmethod
    def random(n=10):
        return Allocation([
            (Person.random(), random.randrange(80, 100))
            for i in range(n)
        ])
    
    def has_conflict(self, request):
        if (request.person in self and self[request.person] != -1) or request.wish() == -1:
            return True
        return any(
            request.is_conflicted_with(person, self[person])
            for person in self
        )
    
    def appended(self, person, allocated_number): # immutable
        result = Allocation(self)
        result[person] = allocated_number
        return result
    
    def extended(self, bucket): # immutable
        result = Allocation(self)
        for request in bucket:
            result[request.person] = request.wish()
        return result
    
    def add_bucket_naively(self, bucket):
        bucket = RequestList(filter(
            lambda r: not self.has_conflict(r),
            bucket
        ))

        good_bucket = RequestList()
        poor_bucket = RequestList()
        
        for request in bucket:
            if any(request.is_conflicted_with(another.person, another.wish())
                for another in bucket
                if another != request
            ):
                poor_bucket.append(request)
            else:
                good_bucket.append(request)
        
        result = self.extended(good_bucket)
        
        if poor_bucket:
            print("There is a conflict among %d people" % len(poor_bucket))
            print("\n".join(map(
                lambda i: "Row %d: %s" % (i, poor_bucket[i]),
                range(len(poor_bucket))
            )))
            print("Enter the ROW NUMBERS of the WINNERS:")
            indexes = map(int, input().split())
            selected_bucket = map(lambda i: poor_bucket[i], indexes)
            result = self.extended(selected_bucket)
        
        return result
    
    def add_bucket_list_naively(self, bucket_list):
        result = self
        for bucket in bucket_list:
            result = result.add_bucket_naively(bucket)
        for bucket in bucket_list:
            for request in bucket:
                if request.person not in result:
                    result[request.person] = -1
        return result

    @staticmethod
    def from_csv(filepath, people):
        try:
            df = pd.read_csv(filepath, header=None, index_col=0)
            keys = df.index.values.tolist()
            values = df.iloc[:, 0].tolist()
            keys = [next(person for person in people if person.id == id) for id in keys]
            return Allocation(zip(keys, values))
        except (FileNotFoundError, pd.errors.EmptyDataError) as e:
            print("NOTE: using empty data, reason: %s" % str(e))
            return Allocation()
    
    def to_csv(self, filepath):
        try:
            copyfile(filepath, filepath + '.bak')
        except FileNotFoundError:
            pass

        mapping = OrderedDict([
            (key.id, value)
            for key, value in self.items()
        ])
        df = pd.DataFrame.from_dict(mapping, orient='index')
        df.to_csv(filepath, header=False)

if __name__ == '__main__':
    people = People.from_csv('SMC_test_output.csv')
    allocation = Allocation.from_csv('allocation.csv', people)
    print(allocation)
    #a = Allocation.random()
    #print(a)
    #b = BucketList.random()
    #print(b)
    #c = a.add_bucket_list_naively(b)
    #print(c)
    
