from math import pi, sqrt
from functools import reduce
import string

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def mySum(l):
    if(l == []):
        return 0
    else:
        return l[0] + mySum(l[1:])

def tower(n):
    if(n == 0):
        return 1
    else:
        return 2**tower(n-1)

def tribonacci(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    elif(n == 2):
        return 2
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
    
