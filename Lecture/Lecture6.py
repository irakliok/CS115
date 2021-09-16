from math import pi, sqrt
from functools import reduce
import string

def abs(n):
    if(n > 0):
        return n
    else:
        return n * -1
    
def maxOutThree(a, b, c):
    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    else:
        return c

def matchFirst(s1, s2):
    return (s1[1] == s2[2])

def isPalindrome(s):
    return (s == s[::-1])

print("Enter the x for one of the following (menu(x)): 1.Coke, 2.Water, 3.Sprite, 4.Bravo, and 5.Fanta")
def menu(n):
    if(n < 1 or n > 5):
        return "Wrong Input"
    elif(n == 1):
        return "Here is your Coke"
    elif(n == 2):
        return "Here is your Water"
    elif(n == 3):
        return "Here is your Sprite"
    elif(n == 4):
        return "Here is your Bravo"
    elif(n == 5):
        return "Here is your Fanta"

def rightTrianglesCount(l):
    x = 0
    if(sqrt(l[0][0]**2 + l[0][1]**2) == l[0][2]):
        x+=1
    if(sqrt(l[1][0]**2 + l[1][1]**2) == l[1][2]):
        x+=1
    if(sqrt(l[2][0]**2 + l[2][1]**2) == l[2][2]):
        x+=1
    return x
       

def inverseSquaresSum(n):
    odd = list(range(1, (n+1), 2))
    return sum(map(inverse, map(sqrt, odd)))
