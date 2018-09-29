#!/usr/bin/env python3

import unittest
from person import Person
from request import Request

class TestStringMethods(unittest.TestCase):

    def test_request(self):
        a = Person(id="A", wave=1, pts=50, opt1=10, opt2=10, opt3=10, sports=["Frisbee"])
        b = Person(id="B", wave=1, pts=50, opt1=10, opt2=10, opt3=10, sports=["Swimming"])
        c = Person(id="C", wave=3, pts=50, opt1=10, opt2=10, opt3=10, sports=["Frisbee"])
        d = Person(id="D", wave=3, pts=50, opt1=10, opt2=10, opt3=10, sports=["Swimming"])
        e = Person(id="E", wave=4, pts=50, opt1=10, opt2=10, opt3=10, sports=["Swimming"])
        self.assertTrue(Request(b, 0).is_conflicted_with(a, 10))
        self.assertTrue(Request(d, 0).is_conflicted_with(a, 10))
        self.assertFalse(Request(d, 0).is_conflicted_with(c, 10))
        self.assertFalse(Request(e, 0).is_conflicted_with(c, 10)) # TODO

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    print("EXPERIMENTAL")
    unittest.main()

