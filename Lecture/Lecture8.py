from math import pi, sqrt
from functools import reduce
import string

def myTuples():
    foo = (42, 'hello', (5, 'spam'), 'penguin')
    print(foo[0])
    print(foo[-1])
    print(foo[0:2])
    print(foo[0:1])

def myDictionary():
    D = {}
    D[x] = y               # x is key, y is value
    # x can be any value
    # y must be immutable type (string, int, tuple of immutables)
    D.keys()
    D.values()
    D.items()
