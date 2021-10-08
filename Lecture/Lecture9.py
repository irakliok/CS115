from math import pi, sqrt
from functools import reduce
import string
import time


def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
memo = {}
def fastFibonacci(n):
    if n in memo:
        return memo[n]
    if n < 0:
        return "Incorrect input"
    elif n == 0:
        memo[n] = 0
        return 0
    elif n == 1 or n == 2:
        memo[n] = 1
        return 1
    else:
        first_term = fastFibonacci(n-1)
        memo[n-1] = first_term
        second_term = fastFibonacci(n-2)
        memo[n-2] = second_term
        return first_term + second_term

def testFibonacci(n):
    print("n is ", n)
    start = time.time()
    slow = Fibonacci(n)
    print("Using Fibonacci - takes", time.time() - start, "seconds")
    start = time.time()
    fast = fastFibonacci(n)
    print("Using fastFibonacci - takes", time.time() - start, "seconds")
    return none



def LCS(S1, S2):
    if S1 == "" or S2 == "":
        return 0
    elif S1[0] == S2[0]:
        return 1 + LCS(S1[1:], S2[1:])
    else:
        return max(LCS(S1, S2[1:]), LCS(S1[1:], S2)
                   
memo2 = {}
def fastLCS(s1, s2):
    if (s1, s2) in memo2:
        return memo2[(s1,s2)]
    elif s1 == "" or s2 == "":
        memo2[(s1,s2)] = 0
        return 0
    elif s1[0] == s2[0]:
        answer = 1 + fastLCS(s1[1:], s2[1:])
        memo2[(s1,s2)] = answer
        return answer
    else:
        chopS1 = fastLCS(s1[1:], s2)
        chopS2 = fastLCS(s1, s2[1:])
        answer = max(chopS1, chopS2)
        memo2[(s1,s2)] = answer
        return answer
