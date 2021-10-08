# more on recursion, filter and lambda functions

"""Irakli Okruashvili
    I pledge my honor that I have abided by the Stevens Honor System - I.O.
    """

def addOne(lon):
    '''Assuming lon is a list of numbers, make a list by adding one to each.
    This is the same as map(add1, lon) where add1 is a function that adds one.
    Your task is to implement it using recursion, not map.'''
    if(lon == []):
        return []
    else:
        return [lon[0]+1] + addOne(lon[1:])

def test_addOne():
    print( addOne([2,2]) == [3,3] )
    print( addOne([]) == [] )

def sumPos(lon):
    '''Assuming lon is a list of number, return the sum of the positive elements,
    ignoring negative ones.  For example, sumPos([1,-3,0,6]) is 7.
    This is the same as sum(filter(isPos,lon)) where isPos checks for positive.'''
    if(lon == []):
        return []
    elif(lon[0] <=1):
        return []
    else:
        return lon[0] + sumPos(lon[1:])
    
def testSumPos():
    print(sumPos([1,2,3,4]) == 6)
    print(sumPos(list(range(10)) == 45))

"""
def prime(n):
    '''whether or not n is prime, assuming n is a non-negative integer'''
    return 0

def testPrime():
    '''print True for each successful test'''
    print(prime(2))
    print(prime(3))
    print(not prime(4))
    print(prime(37))
    print(not prime(39))
"""
