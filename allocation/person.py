#!/usr/bin/env python3

import sys

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


def get_people():
    people = {}
    for line in sys.stdin:
        if line.strip() != "":
            person = Person(line)
            people[person.id] = person
        else:
            break
    return people
