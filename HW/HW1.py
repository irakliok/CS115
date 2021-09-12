from math import pi, sqrt
from functools import reduce
import string

"""Irakli Okruashvili
    I pledge my honor that I have abided by the Stevens Honor System - I.O."""

def mult(x, y):
    return x*y;

def factorial(n):
    return reduce(mult, list(range(1, n+1)))
