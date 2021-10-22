import time

''' I pledge my honor that I have abided by the Stevens Honor System
        - Irakli Okruashvili'''

"""Kung Fu Panda has a number of staircases he needs to climb.
He likes to climb each staircase 1, 2, or 3 steps at a time.
Being a very precocious character, he wonders how many ways there are to reach
the top of the staircase. Your help is needed here. 
"""

"""
1. Write a recursive function KFP_slow that will take as an input a positive
integer denoting the number of stairs and will return the number of ways
Kung Fu Panda can climb those stairs.
"""
def KFP_slow(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        OneStep = 1 + KFP_slow(n - 1)
        TwoStep = 1 + KFP_slow(n - 2)
        ThreeStep = 1 + KFP_slow(n - 3)
        return OneStep + TwoStep + ThreeStep
        
print(KFP_slow(5))
print(KFP_slow(30))


"""
2. Use memoization to speed up your solution of KFP_slow.
"""
memo = {1:1, 2:2, 3:4}
def KFP_fast(n):
    if n in memo:
        return memo[n]
    ans1 = KFP_fast(n-1)
    memo[n-1] = ans1
    ans2 = KFP_fast(n-2)
    memo[n-2] = ans2
    ans3 = KFP_fast(n-3)
    memo[n-3] = ans1
    return ans1 + ans2 + ans3

    
print(KFP_fast(5))
print(KFP_fast(30))


"""
3. Write a function called MeasureTime that takes as an input a function f and a integer n and returns the time needed for function f to finish runnig when given the input n
"""

import time
def MeasureTime(f, n):
    start = time.time()
    f(n)
    return time.time() - start
    

print("KFP slow takes: ", round(MeasureTime(KFP_slow, 30),2), "secs")
print("KFP fast takes: ", round(MeasureTime(KFP_fast, 30),6), "secs")

