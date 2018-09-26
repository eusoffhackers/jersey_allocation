#!/usr/bin/env python3

from itertools import groupby

class Request:
    # personID, rank (0..2), pts, wish

    def __init__(self, person, rank):
        self.personID = person.id
        self.rank = rank
        self.pts = person.pts
        wishes = [person.opt1, person.opt2, person.opt3]
        self.wish = wishes[rank]

    def __repr__(self):
        return ("Request(personID = %d, rank = %d, pts = %d, wish = %d)"
                % (self.personID, self.rank, self.pts, self.wish))

def get_requests(people):
    requests = []

    for id, person in people.items():
        for rank in range(3):
            requests.append(Request(person, rank))

    def key_function(r):
        return (r.rank, r.pts, r.wish)

    requests = sorted(requests, key=key_function)
    return requests

def get_buckets(requests):
    # returns list of list of requests

    def key_function(r):
        return (r.rank, r.pts, r.wish)

    groups = groupby(requests, key_function)
    return [list(g) for k, g in groups]
