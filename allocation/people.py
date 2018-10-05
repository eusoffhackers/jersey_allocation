#!/usr/bin/env python3

import sys
import pandas as pd
import collections
from person import Person, MALE, FEMALE

class People(list):
    
    def __str__(self):
        header = "People (len=%d)\n" % len(self)
        return header + '\n'.join(map(str, self))
    
    @staticmethod
    def random(n=50):
        return People([Person.random() for i in range(n)])
    
    @staticmethod
    def from_csv(filepath):
        keep = {
            "full": 'id',
            "wave": 'wave',
            "first": 'opt1',
            "second": 'opt2',
            "third": 'opt3',
            "total_points": 'pts',
            "gender": 'gender',
            "sports": 'sports'
        }
        df = pd.read_csv(filepath, dtype=str).fillna('')
        df = df.rename(lambda s: str(s).partition(' ')[0].lower(), axis='columns')
        df = df.rename(columns=keep)[list(keep.values())]
        assert set(df) == set(keep.values())
        
        people = People([
            Person.from_series(row)
            for index, row in df.iterrows()
        ])
        
        return people
    
    def get_summary_text(self):
        male_count = sum(1 for person in self if person.gender == MALE)
        female_count = sum(1 for person in self if person.gender == FEMALE)
        wave_count = collections.Counter([person.wave for person in self])
        return "\n".join([
            "There are %d people, %d men, %d women" % (len(self), male_count, female_count),
            "    Wave 1: %d people" % (wave_count.get(1, 0)),
            "    Wave 2: %d people" % (wave_count.get(2, 0)),
            "    Wave 3: %d people" % (wave_count.get(3, 0)),
            "    Wave 4: %d people" % (wave_count.get(4, 0))
        ])

if __name__ == '__main__':
    print(People.from_csv('SMC_test_output.csv'))
    print(People.random())
