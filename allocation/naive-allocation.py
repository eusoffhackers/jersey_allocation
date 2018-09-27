#!/usr/bin/env python3

PEOPLE_CSV = 'SMC_test_output.csv'
ALLOCATION_CSV = 'allocation.csv'

from people import People
from requestlist import RequestList
from bucketlist import BucketList
from allocation import Allocation

people = People.from_csv(PEOPLE_CSV)
print(people)

allocation = Allocation.from_csv(ALLOCATION_CSV, people)
print(allocation)

wave = int(input("Wave (1, 2, 3, 4, 5): "))
people_in_wave = People(filter(lambda person: person.wave == wave, people))
request_list = RequestList.from_people(people_in_wave)
bucket_list = BucketList.from_request_list(request_list)
allocation = allocation.add_bucket_list_naively(bucket_list)
print(allocation)

can_save = input("Save to %s [yN]: " % ALLOCATION_CSV).lower() == 'y'

if can_save:
    allocation.to_csv(ALLOCATION_CSV)
    print("Saved to %s." % ALLOCATION_CSV)
else:
    print("Will not save to %s." % ALLOCATION_CSV)
