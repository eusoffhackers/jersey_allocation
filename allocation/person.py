#!/usr/bin/env python3

import sys, random, string
from collections import OrderedDict

SPORTS = ["Badminton", "Basketball", "Floorball", "Frisbee",
    "Handball", "Netball", "Road Relay", "Sepak Takraw", "Soccer",
    "Softball", "Squash", "Swimming", "Table Tennis", "Tennis",
    "Touch Rugby", "Track", "Volleyball"]

NO_SPORTS = ["NIL"]
MIXED_SPORTS = ["Frisbee", "Swimming", "Track", "Road Relay", "Softball"]
GENDERS = ["Male", "Female"]

class Person:
    """
    person1 = Person(
        id="ABC", wave=1, pts=10, opt1=98, opt2=76, opt3=54,
        sports=["Swimming M", "Football M", "Frisbee", "Sepak Takraw"],
    )
    """
    
    def __init__(self, **kwargs):
        required_keys = {"id", "wave", "pts", "opt1", "opt2", "opt3", "sports"}
        assert required_keys <= set(kwargs.keys())
        self.__dict__.update(kwargs)

    def __repr__(self):
        shorten_gender = lambda gender: gender[0] if gender in GENDERS else "X"
        shorten = lambda sp: sp[:3] + shorten_gender(sp.split()[-1])
        sports = '+'.join(map(shorten, self.sports))
        return "Person(%s, wave=%01d, pts=%02d, %02d, %02d, %02d, %s)" % (
            self.id, self.wave, self.pts, self.opt1, self.opt2, self.opt3, sports
        )
    
    def wish(self, rank):
        assert rank in [0, 1, 2]
        return [self.opt1, self.opt2, self.opt3][rank]

    '''
    @staticmethod
    def from_string(line):
        a = [s.strip() for s in line.split(',')]
        return Person(
            id=a[0], name=a[1], pts=int(a[2]),
            opt1=int(a[3]), opt2=int(a[4]), opt3=int(a[5])
        )
    '''
    
    @staticmethod
    def parse_sports(raw_sports, gender):
        assert gender in GENDERS
        if raw_sports in NO_SPORTS:
            return []
        sports = raw_sports.split(', ')
        assert set(sports) <= set(SPORTS)
        return [
            sp if sp in MIXED_SPORTS else sp + " " + gender
            for sp in sports
        ]
    
    @staticmethod
    def from_series(row):
        to_int_def = lambda x, default: int(str(x)) if str(x).isdigit() else default

        result = Person(
            id = row['id'],
            wave = to_int_def(row['wave'], -1),
            pts = to_int_def(row['pts'], 0),
            opt1 = to_int_def(row['opt1'], -1),
            opt2 = to_int_def(row['opt2'], -1),
            opt3 = to_int_def(row['opt3'], -1),
            sports = Person.parse_sports(row['sports'], row['gender'])
        )
        
        assert result.wave in [1, 2, 3, 4, 5]
        assert str(row['opt1']) == "" or result.opt1 != -1, "Cannot parse '%s'" % str(row['opt1'])
        assert str(row['opt2']) == "" or result.opt2 != -1, "Cannot parse '%s'" % str(row['opt2'])
        assert str(row['opt3']) == "" or result.opt3 != -1, "Cannot parse '%s'" % str(row['opt3'])
        
        return result
    
    @staticmethod
    def random():
        __randstr = lambda n: ''.join(random.choices(string.ascii_uppercase, k=n))
        return Person(
            id = __randstr(8),
            wave = random.randrange(1, 5),
            name = (__randstr(4) + " " + __randstr(4)).title(),
            pts = random.randrange(10, 20),
            opt1 = random.randrange(80, 100),
            opt2 = random.randrange(80, 100),
            opt3 = random.randrange(80, 100),
            sports = [
                sp + " " + random.choice(GENDERS)
                for sp in random.sample(SPORTS, 3)
            ]
        )

if __name__ == '__main__':
    for i in range(50):
        b = Person.random()
        print(b)
