'''
Created on 10/22/21
@author:   Irakli Okruashvili
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
            - I.O.

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def numToBin(n):
    '''n must be non-negative.
    Returns the string with the binary representation of n.'''
    if n == 0:
        return ""
    elif n%2 == 0:
        return numToBin(n/2) + "0"
    elif n%2 == 1:
        return numToBin(n//2) + "1"

def binToNum(S):
    '''s must be a string of 0s and 1s.
    Returns the integer value of the binary representation in s.'''
    if S == '':
        return 0
    else:
        return int(S[-1]) + 2*binToNum(S[:-1])

def binaryPadded(n):
    '''Pads zeros in front of the binary string for a length.'''
    S = numToBin(int(n))
    return "0"*(COMPRESSED_BLOCK_SIZE - len(S)) + S

def prefixLength(S):
    '''Returns the padded value of a string'''
    if len(S) == 1:
        return 1
    if S[0] != S[1]:
        return 1
    return 1 + prefixLength(S[1:])

def compress(S):
    '''returns a run-length encoding of the 64 bit input string.'''
    def compress_help(S,x):
        if S == "":
            return ""
        if S[0] != chr(x+ord("0")):
            return binaryPadded("0") + compress_help(S,1-x)
        else:
            length = prefixLength(S)
            length = min(length,MAX_RUN_LENGTH)
            return binaryPadded(length)+compress_help(S[length:],1-x)
    return compress_help(S,0)


def uncompress(C):
    '''returns an inversion or undoing the compressed string.'''
    if C == "":
        return ""
    if len(C) == COMPRESSED_BLOCK_SIZE:
        return binToNum(C)*"0"
    else:
        return binToNum(C[0:5])*"0" + binToNum(C[5:10])*"1" + uncompress(C[10:])
    
def compression(S):
    '''gives the ratio of the compress string to the uncompressed string'''
    if len(S) == 0:
        return
    return  len(compress(S)) / len(S)
