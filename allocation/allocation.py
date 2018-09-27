#!/usr/bin/env python3

import sys, random
import pandas as pd
from collections import OrderedDict
#from shutil import copyfile
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
        if request.person in self:
            return True
        if request.wish() < 1 or request.wish() > 99:
            return True
        for person in self:
            if request.wish() == self[person]:
                if bool(set(request.person.sports) & set(person.sports)):
                    print(set(request.person.sports), set(person.sports), bool(set(request.person.sports) & set(person.sports)))
                    return True
        return False
    
    def add(self, person, wish):
        result = Allocation(self)
        result[person] = wish
        return result
    
    def add_bucket_naively(self, bucket):
        bucket = RequestList(filter(lambda r: not self.has_conflict(r), bucket))
        if not bucket:
            return self
        elif len(bucket) == 1:
            request = bucket[0]
            return self.add(request.person, request.wish())
        else:
            print("There is a conflict among %d people" % len(bucket))
            print("\n".join(map(str, bucket)))
            print("Enter the row number of the winner:")
            request = bucket[int(input())]
            return self.add(request.person, request.wish())
    
    def add_bucket_list_naively(self, bucket_list):
        result = self
        for bucket in bucket_list:
            result = result.add_bucket_naively(bucket)
        return result

    """
    @staticmethod
    def from_stdin():
        allocation = Allocation()
        for line in sys.stdin:
            if line == '':
                continue
            tokens = line.split(' ')
            id, number = tokens[0], int(tokens[1])
            allocation[id] = number
        return allocation
    """

    @staticmethod
    def from_csv(filepath, people):
        try:
            df = pd.read_csv(filepath, header=None, index_col=0)
            return Allocation(df[1].to_dict(OrderedDict))
        except (FileNotFoundError, pd.errors.EmptyDataError) as e:
            print("NOTE: using empty data, reason: %s" % str(e))
            return Allocation()
"""
    def save_to_csv(self, filepath):
        try:
            copyfile(filepath, filepath + '.bak')
        except FileNotFoundError:
            pass

        df = pandas.DataFrame.from_dict(self.allocation, orient='index')
        df.to_csv(filepath, header=False)
"""

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
    
