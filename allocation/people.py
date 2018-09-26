#!/usr/bin/env python3

import sys
from person import Person

class People(list):
    
    def __init__(self, source = []):
        super(People, self).__init__(source)
    
    def __str__(self):
        return '\n'.join(map(str, self))
    
    @staticmethod
    def from_stdin():
        people = People()
        
        for line in sys.stdin:
            if line.strip() != "":
                person = Person.from_string(line)
                people.append(person)
            else:
                break
        return people

if __name__ == '__main__':
    a = People.from_stdin()
    print(a)

"""

Example input:

101, Kien, 10, 111, 222, 333
102, Julien, 10, 111, 333, 444
103, Eeshan, 10, 333, 444, 555

"""
