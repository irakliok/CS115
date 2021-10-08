# Functions we studied before, and alternate
# definitions using lambda.

"""Irakli Okruashvili
    I pledge my honor that I have abided by the Stevens Honor System - I.O.
    """

def divisibles(L, n):
    '''assume L is a list of integers;
       return a list of the ones divisible by n'''
    if L==[]:
        return []
    elif L[0] % n == 0:
        return [L[0]] + divisibles(L[1:], n)
    else:
        return divisibles(L[1:], n)

def divisibles_alt(L, n):
    '''the divisibles function, using lambda'''
    return list(filter(lambda m: m%n == 0, L))
           

def test_divisibles():
    print ( divisibles([3,6,4,9], 3) == [3,6,9] )
    print ( divisibles_alt([3,6,4,9], 3) == [3,6,9] )


''' --------- '''

def inc_all(nums, n):
    '''Add n to every number in a given list of numbers.'''
    if nums == []:
        return []
    else:
        return [nums[0]+n] + inc_all(nums[1:], n)

def inc_all_alt(nums, n):
    '''the inc_all function, using lambda'''
    return list(map(lambda k: k + n, nums))

def test_inc_all():
    '''Tests for inc_all. Correct tests print True.'''
    print(inc_all([1, 3, 5], 2) == [3, 5, 7])
    print(inc_all([-2, -1, 0, 1, 2], 10) == [8, 9, 10, 11, 12])
    print(inc_all_alt([1, 3, 5], 2) == [3, 5, 7])
    print(inc_all_alt([-2, -1, 0, 1, 2], 10) == [8, 9, 10, 11, 12])







