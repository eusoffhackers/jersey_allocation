#!/usr/bin/env python3

PEOPLE_CSV = 'SMC_test_output.csv'
ALLOCATION_CSV = 'allocation.csv'

from people import People
from requestlist import RequestList
from bucketlist import BucketList
from allocation import Allocation, conflict_list
from allocationlist import AllocationList

people = People.from_csv(PEOPLE_CSV)
print(people.get_summary_text())

allocation = Allocation.from_csv(ALLOCATION_CSV, people)
print(allocation.get_summary_text())

allocation_list = AllocationList([allocation])

wave = int(input("Wave (1, 2, 3, 4): "))
people_in_wave = People(filter(lambda person: person.wave == wave, people))
request_list = RequestList.from_people(people_in_wave)
bucket_list = BucketList.from_request_list(request_list)

allocation_list = allocation_list.add_bucket_list(bucket_list)
allocation = allocation_list.flatten()

print("\nDone.\n")
print(allocation.get_summary_text())

if conflict_list:
    print("List of conflicted requests (in order):")
    print("\n".join(map(str, conflict_list)))
else:
    print("There are no conflicts.")

can_save = input("Save to %s [yN]: " % ALLOCATION_CSV).lower() == 'y'

if can_save:
    allocation.to_csv(ALLOCATION_CSV)
    print("Saved to %s." % ALLOCATION_CSV)
else:
    print("Will not save to %s." % ALLOCATION_CSV)
