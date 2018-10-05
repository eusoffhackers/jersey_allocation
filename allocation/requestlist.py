#!/usr/bin/env python3

from request import Request
from people import People

class RequestList(list):

    def __str__(self):
        header = "RequestList (len=%d)\n" % len(self)
        return header + '\n'.join(map(str, self))
    
    def __sub__(self, other):
        return RequestList([item for item in self if item not in other])
    
    @staticmethod
    def from_people(people):
        requests = [Request(person, rank)
            for person in people
            for rank in range(3)]
        requests = sorted(requests, key = Request.key)
        return RequestList(requests)
    
    @staticmethod
    def random():
        return RequestList.from_people(People.random(5))
    
    def is_independent(self, request):
        return not any(
            request.is_conflicted_with(another.person, another.wish())
            for another in self
            if another != request
        )
    
    def get_independent_requests(self):
        return RequestList(filter(self.is_independent, self))    
    
    def all_subsets(self):
        sets = []
        for i in range(1 << len(self)):
            subset = RequestList([self[bit] for bit in range(len(self)) if (1 << bit) & i])
            sets.append(subset)
        return sets
    
if __name__ == '__main__':
    a = RequestList.random()
    print(a)
    print(a.get_independent_requests())
    
