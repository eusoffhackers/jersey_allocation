#!/usr/bin/env python3

import sys
import pandas as pd
from person import Person

class People(list):
    
    def __str__(self):
        header = "People (len=%d)\n" % len(self)
        return header + '\n'.join(map(str, self))
    
    '''
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
    '''
    
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

if __name__ == '__main__':
    print(People.from_csv('SMC_test_output.csv'))
    print(People.random())
    #a = People.from_stdin()
    #print(a)

"""

Example input:

101, Kien, 10, 111, 222, 333
102, Julien, 10, 111, 333, 444
103, Eeshan, 10, 333, 444, 555

"""
