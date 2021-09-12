from math import pi, sqrt
from functools import reduce

name="Irakli"

def dbl(n):
    return 2*n

def add(x,y):
    return x+y

def square(x):
    return x*x



def evens(x):
    nums = list(range(x+1))
    return list(map(dbl, nums))

def span(x):
    minimum = reduce(min, x)
    maximum = reduce(max, x)
    return maximum - minimum

def gauss(x):
    l = list(range(x+1))
    return reduce(add, l)

def sumOfSquares(x):
    l = list(range(x+1))
    return reduce(add, map(square, l))

def distance(x,y):
    return sqrt((y[0]-x[0])**2 + (y[1]-x[1])**2)
