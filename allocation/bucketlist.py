#!/usr/bin/env python3

from itertools import groupby
from requestlist import RequestList

class BucketList(list):
    
    def __str__(self):
        header = "BucketList (len=%d)\n" % len(self)
        return header + '\n'.join(map(str, self))
    
    @staticmethod
    def from_request_list(request_list):
        fn = lambda r: (r.person.wave, r.rank, r.person.pts, r.person.wish(r.rank))
        groups = groupby(request_list, fn)
        buckets = [RequestList(g) for k, g in groups]
        return BucketList(buckets)
    
    @staticmethod
    def random():
        return BucketList.from_request_list(RequestList.random())

if __name__ == '__main__':
    print(BucketList.random())
