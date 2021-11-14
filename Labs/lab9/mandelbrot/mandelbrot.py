# mandelbrot.py
# Lab 9
# Name: Irakli Okruashvili

'''
11/4/21
Irakli Okruashvili
I pledge my honor that I have abided by the Stevens Honor System
    - Irakli Okruashvili
'''

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:
def mult( c, n ):
    '''
        mult uses only a loop and addition
        to multiply c by the integer n
    '''
    result = 0
    for x in range(n): # update the value of result here in the loop
        result = result+c
    return result

def update(c,n):
    '''
        update starts with z=0 and runs z = z**2 + c
        for a total of n times.
        It returns the final z.
    '''
    z=0
    for x in range(n):
        z = z**2 + c
    return z

def inmset(c,n):
    '''
        inMSet takes in
        c for the update step of z = z**2+c
        n, the maximum number of times to run that step
        Then, it should return
        False as soon as abs(z) gets larger than 2
        True if abs(z) never gets larger than 2 (for n iterations)
    '''
    z=0
    for x in range(n):
        z = z**2 + c
        if abs(z) > 2: return False
    return True
    
def scale(pix,pixMax,floatMin,floatMax):
    '''
        scale takes inpix,
        the CURRENT pixel column (or row)
        pixMax, the total # of pixel columns
        floatMin, the min floating-point value
        floatMax, the max floating-point value
        scale returns the floating-point value that
        corresponds to pix
    '''
    r = pix/pixMax
    return floatMin + r*(floatMax - floatMin)
    
def mset():
    width=300
    height=200
    image=PNGImage(width,height)
    for col in range(width):
        for row in range(height):
            x = scale(col,width,-2,1)
            y = scale(row,height,-1,1)
            c = x + y*1j
            if inmset(c,25):
                image.plotPoint(col, row)
    image.saveFile()

mset()
