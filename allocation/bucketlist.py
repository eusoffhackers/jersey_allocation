#!/usr/bin/env python3

from itertools import groupby
from requestlist import RequestList
from request import Request

class BucketList(list):
    
    def __str__(self):
        header = "BucketList (len=%d)\n" % len(self)
        return header + '\n'.join(map(str, self))
    
    @staticmethod
    def from_request_list(request_list):
        groups = groupby(request_list, Request.key)
        buckets = [RequestList(g) for k, g in groups]
        return BucketList(buckets)
    
    @staticmethod
    def random():
        return BucketList.from_request_list(RequestList.random())

if __name__ == '__main__':
    print(BucketList.random())
