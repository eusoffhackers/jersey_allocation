#!/usr/bin/env python3

from request import Request
from people import People

class RequestList(list):

    def __str__(self):
        header = "RequestList (len=%d)\n" % len(self)
        return header + '\n'.join(map(str, self))
    
    @staticmethod
    def from_people(people):
        requests = [Request(person, rank)
            for person in people
            for rank in range(3)]
        fn = lambda r: (r.rank, r.person.pts, r.person.wish(r.rank))
        requests = sorted(requests, key = fn)
        return RequestList(requests)
    
    @staticmethod
    def random():
        return RequestList.from_people(People.random())
    
if __name__ == '__main__':
    print(RequestList.random())
