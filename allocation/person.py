#!/usr/bin/env python3

import sys, random, string
from collections import OrderedDict

class Person:
    """
    person1 = Person(
        id="ABC",
        name="Kien Nguyen",
        pts=10,
        opt1=98,
        opt2=76,
        opt3=54
    )
    """
    
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return "Person(%s, %s, %d, %d, %d, %d)" % (
            self.id, self.name, self.pts,
            self.opt1, self.opt2, self.opt3,
        )
    
    def wish(self, rank):
        return [self.opt1, self.opt2, self.opt3][rank]

    @staticmethod
    def from_string(line):
        a = [s.strip() for s in line.split(',')]
        return Person(
            id=a[0], name=a[1], pts=int(a[2]),
            opt1=int(a[3]), opt2=int(a[4]), opt3=int(a[5])
        )
    
    @staticmethod
    def random():
        __randstr = lambda n: ''.join(random.choices(string.ascii_uppercase, k=n))
        return Person(
            id = __randstr(8),
            name = (__randstr(4) + " " + __randstr(4)).title(),
            pts = random.randrange(10, 20),
            opt1 = random.randrange(80, 100),
            opt2 = random.randrange(80, 100),
            opt3 = random.randrange(80, 100)
        )

if __name__ == '__main__':
    b = Person.random()
    print(b)
