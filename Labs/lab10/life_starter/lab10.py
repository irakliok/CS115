#
# life.py - Game of Life lab
#
# Name: Irakli Okruashvili
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.- I.O.
#

import random

def createOneRow(width):
    """ Returns one row of zeros of width "width"...  
        You should use this in your
        createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row
def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)] # What do you need to add a whole row here?
    return A
def printBoard( A ):
    """ this function prints the 2d list-of-lists
        A without spaces (using sys.stdout.write)"""
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )
def diagonalize(width,height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells."""
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A
def innerCells(w,h):
    ''' returns a board with a border of 0s and 1s inside'''
    A = createBoard( w, h )
    for row in range(1,h-1):
        for col in range(1,w-1):
            if row == 0 or col == 0:
                A[row][col] = 0
            else:
                A[row][col] = 1
    return A
def randomCells(w,h):
    ''' returns a board with random 0s and 1s inside'''
    A = createBoard( w, h )
    for row in range(1,h-1):
        for col in range(1,w-1):
            if row == 0 or col == 0:
                A[row][col] = 0
            else:
                A[row][col] = random.choice( [0,1] )
    return A
def copy( A ):
    ''' returns a deep copy of a board'''
    B = createBoard(len(A[0]),len(A))
    for row in range(len(A)):
        for col in range(len(A[0])):
            B[row][col] = A[row][col]
    return B
def innerReverse( A ):
    ''' returns a board that switches the inner 0s and 1s in A'''
    B = copy ( A )
    for row in range(1,len(A)-1):
        for col in range(1,len(A[0])-1):
            if B[row][col] == 0:
                B[row][col] = 1
            elif B[row][col] == 1:
                B[row][col] = 0
    return B

def next_life_generation( A ):
    """ makes a copy of A and then advanced one
        generation of Conway's game of life within
        the *inner cells* of that copy.
        The outer edge always stays 0."""
    def countNeighbors( row, col, A ):
        ''' returns number of live neighbors for a cell
        in board A at a particular row and col'''
        total = 0
        for y in range(col-1,col+2):
            for x in range(row-1,row+2):
                if A[x][y] == 0:
                    total = total + 0
                elif A[x][y] == 1:
                    total = total + 1
        return total - A[row][col]

    newA = copy(A)
    for row in range(1,len(A)-1):
        for col in range(1,len(A[0])-1):
            if A[row][col] == 1 and countNeighbors( row, col, A ) < 2:
                newA[row][col] = 0
            elif A[row][col] == 1 and countNeighbors( row, col, A ) > 3:
                newA[row][col] = 0
            elif A[row][col] == 0 and countNeighbors( row, col, A ) == 3:
                newA[row][col] = 1
    return newA
