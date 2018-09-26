#!/usr/bin/env python3

import sys
import pandas
import copy
from collections import OrderedDict
from shutil import copyfile

class Allocation:

    def __init__(self):
        self.allocation = OrderedDict()

    def __repr__(self):
        return str(self.allocation)
    
    def clone(self):
        return copy.deepcopy(self)

    def load_from_stdin(self):
        for line in sys.stdin:
            if line == '':
                continue
            tokens = line.split(' ')
            id, number = tokens[0], int(tokens[1])
            self.allocation[id] = number

    def load_from_csv(self, filepath):
        try:
            df = pandas.read_csv(filepath, header=None, index_col=0)
            self.allocation = df[1].to_dict(OrderedDict)
        except FileNotFoundError:
            print("{} not found, fallback to empty data", filepath)
            self.allocation = OrderedDict()

    def save_to_csv(self, filepath):
        try:
            copyfile(filepath, filepath + '.bak')
        except FileNotFoundError:
            pass

        df = pandas.DataFrame.from_dict(self.allocation, orient='index')
        df.to_csv(filepath, header=False)

if __name__ == '__main__':
    a = Allocation()
    #a.load_from_stdin()
    a.load_from_csv('test.csv')
    print(a)
    a.save_to_csv('test.csv')
