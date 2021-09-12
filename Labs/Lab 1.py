from math import pi, sqrt, factorial
from functools import reduce

"""Irakli Okruashvili
    I pledge my honor that I have abided by the Stevens Honor System - I.O.
    """


""" reciprocal function"""
def inverse(n):
    return float(1/n)

""" 1 + 1/1! + 1/2! + 1/3! + 1/n!"""
def e(n):
    return sum(map(inverse, map(factorial,list(range(1, n+1)))))

