#!/usr/bin/env python3

from person import Person

class Request:

    def __init__(self, person, rank):
        assert rank in [0, 1, 2]
        self.person = person
        self.rank = rank
        
    def __repr__(self):
        return ("Request(person = %s, rank = %s)" % (self.person, self.rank))
    
    def wish(self):
        return self.person.wish(self.rank)

if __name__ == '__main__':
    r = Request(Person.random(), 2)
    print(r)
