#!/usr/bin/env python3

from allocation import Allocation, conflict_list
from collections import OrderedDict

class AllocationList(list):
    
    def add_bucket(self, bucket):
        return AllocationList([
            sub_allocation
            for allocation in self
            for sub_allocation in allocation.add_bucket_smart(bucket)
        ])
    
    def add_bucket_list(self, bucket_list):
        ttl = 10000
        result = self
        
        for bucket in bucket_list:
            ttl -= len(result)
            print("Number of branches: %d. TTL = %d" % (len(result), ttl))
            if ttl < 0:
                print("List of conflicted requests (in order):")
                print("\n".join(map(str, conflict_list)))
                print("Computation took a long time. You can stop to get partial result.")
                print("Resolve found conflicts then run the script again")
                if input("Continue the program? [yN] ") == 'y':
                    ttl += 10000
                else:
                    break
            result = result.add_bucket(bucket)
            
        return AllocationList([
            allocation.mark_unallocated(bucket_list)
            for allocation in result
        ])
    
    def flatten(self):
        result = OrderedDict()
        
        for allocation in self:
            for person in allocation:
                if person not in result:
                    result[person] = set([])
                result[person].add(allocation[person])
        
        target = OrderedDict()
        for person in result:
            if len(result[person]) == 1:
                target[person] = list(result[person])[0]
            else:
                target[person] = -2
        return Allocation(target)
                
