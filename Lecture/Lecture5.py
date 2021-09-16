from math import pi, sqrt
from functools import reduce
import string

name="Irakli"

def dbl(n):
    return 2*n

def add(x,y):
    return x+y

def square(x):
    return x*x

def inverse(n):
    return float(1/n)


def addTwoDigits(n):
    return n//10 + n%10

def largestNumber(n):
    return 10**n-1

def reverse(l):
    l.reverse()
    return l

def headtail(n):
    l = list(range(1, n+1))
    return list(map(square, l))

def longestString(l):
    return max(l, key=len)

def inverseSquaresSum(n):
    odd = list(range(1, (n+1), 2))
    return sum(map(inverse, map(sqrt, odd)))
