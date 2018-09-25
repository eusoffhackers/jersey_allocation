#!/usr/bin/env python3

import sys
from itertools import groupby

class Person:
    # id, name, pts, opt1, opt2, opt3
    
    def __init__(self, line):
        tokens = [s.strip() for s in line.split(',')]
        self.id = int(tokens[0])
        self.name = tokens[1]
        self.pts = int(tokens[2])
        self.opt1 = int(tokens[3])
        self.opt2 = int(tokens[4])
        self.opt3 = int(tokens[5])
    
    def __str__(self):
        return "(%d, %s, %d)" % (self.id, self.name, self.pts)

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

def get_people():
    people = {}
    for line in sys.stdin:
        if line.strip() != "":
            person = Person(line)
            people[person.id] = person
        else:
            break
    return people

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

people = get_people()
requests = get_requests(people)
buckets = get_buckets(requests)

allocated = {} # key: personID, value: wish (jersey number)

def filtered(requests, allocated):
    
    def filter_function(request):
        for personID in allocated: # TODO: check the teams also
            if (request.personID == personID or
                    request.wish == allocated[personID] and True):
                return False
        return True
    
    return list(filter(filter_function, requests))

for bucket in buckets:
    requests = filtered(bucket, allocated)
    if not requests:
        pass
    elif len(requests) == 1:
        r = requests[0]
        allocated[r.personID] = r.wish
    else:
        print("There is a conflict among %d people" % len(requests))
        print("\n".join(map(str, requests)))
        print("Enter the ID of the winner:")
        winnerID = int(input())
        r = list(filter(lambda r: r.personID == winnerID, requests))[0]
        allocated[r.personID] = r.wish

print(allocated)

"""
Example input:
101, Kien, 10, 111, 222, 333
102, Julien, 10, 111, 333, 444
103, Eeshan, 10, 333, 444, 555
"""
