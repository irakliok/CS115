from math import pi, sqrt, factorial
from functools import reduce

"""Irakli Okruashvili
    I pledge my honor that I have abided by the Stevens Honor System - I.O.
    """


"""Dot product: Input(2 lists), Output(dot product)"""
def dot(L,K):
    if(L == [] or K == []):
        return 0
    return L[0]*K[0] + dot(L[1:],K[1:])

"""Return every letter as list: input(string), Output(list of characters)"""
def explode(S):
    if(S == ""):
        return []
    return [S[0]] + explode(S[1:])

"""Finds e in list L"""
def ind(e, L):
    if(L == [] or L == ""):
        return 0
    elif(L[0] == e):
        return 0
    else:
        return ind(e, L[1:]) + 1

"""Removes e from list L"""
def removeAll(e, L):
    if(L == []):
        return []
    elif(L[0] == e):
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])

"""Returns elements of L equal to f"""
def myFilter(f, L):
    if(L == []):
        return []
    elif(f(L[0])):
        return [L[0]] + myFilter(f, L[1:])
    else:
        return myFilter(f, L[1:])

"""Returns reversed list L"""
def deepReverse(L):
    if(L == []):
        return []
    elif(isinstance(L[0], list)):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
        return deepReverse(L[1:]) + [L[0]]
