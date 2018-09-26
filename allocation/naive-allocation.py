#!/usr/bin/env python3

from person import Person, get_people
from request import Request, get_requests, get_buckets

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
