#!/usr/bin/env python3

from itertools import groupby
from person import Person

class Request:

    def __init__(self, person, rank):
        assert rank in [0, 1, 2]
        self.person = person
        self.rank = rank
        
    def __repr__(self):
        return ("Request(person = %s, rank = %s)" % (self.person, self.rank))

def get_buckets(requests):
    # returns list of list of requests

    def key_function(r):
        return (r.rank, r.pts, r.wish)

    groups = groupby(requests, key_function)
    return [list(g) for k, g in groups]

if __name__ == '__main__':
    r = Request(Person.random(), 2)
    print(r)
