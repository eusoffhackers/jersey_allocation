#!/usr/bin/env python3

PEOPLE_CSV = 'SMC_test_output.csv'
ALLOCATION_CSV = 'allocation.csv'

from people import People
from requestlist import RequestList
from bucketlist import BucketList
from allocation import Allocation

people = People.from_csv(PEOPLE_CSV)
waves = list(map(int, input("Waves (1, 2, 3, 4, 5): ").split()))
people = People(filter(lambda person: person.wave in waves, people))
sharable = input("Sharable [yN]: ").lower() == 'y'
print(people)

request_list = RequestList.from_people(people)
bucket_list = BucketList.from_request_list(request_list)
allocation = Allocation.from_csv(ALLOCATION_CSV, people)
allocation = allocation.add_bucket_list_naively(bucket_list, sharable)
print(allocation)

"""
Example input:
101, Kien, 10, 111, 222, 333
102, Julien, 10, 111, 333, 444
103, Eeshan, 10, 333, 444, 555
"""
