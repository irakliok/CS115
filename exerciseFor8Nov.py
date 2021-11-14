# class exercise using for-loop

def mapSqr(L):
    '''Assume L is a list of numbers; return map(sqr,L).
    Use a for-loop.'''
    squares = [i*i for i in L]
    return squares

def testMapSqr():
    assert mapSqr([1,2,3]) == list(map(lambda x: x*x, [1,2,3]))
    
