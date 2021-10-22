'''Irakli Okruashvili
I pledge my honor that I have abidede by the stevens honor system'''


###Solve the following problems. Put the solutions as comments
# 1. What is the binary represantion of 37?
00100101
# 2. What is the base 10 representation of 10101110?
174
# 3. What is the base 10 representation of 1.1011?

# 4. Assume that we have only 8 bits to represent numbers
#    apply two's compliment to represent -17.
10001001
###


### Solve the following map/reduce/filter exercise
# You can use 'in', len, map, filter, and reduce, but try to solve it without
# using fancy Python library functions.

from functools import reduce

Vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

S = '''On this first Monday of October, students and adults alike
are encouraged to BlueUp by wearing our blue shirt or their own
to make that the day that bullying prevention is heard around the world
We chose blue because in many diverse cultures blue brings peace
'''

listOfWords = S.split()

def deVowel(w):
    """Assuming w is a word, remove its vowels.
    For example, deVowel('friday') is 'frdy'."""
    return list(filter(lambda x: x not in Vowels, w))
    

'''Now, change the expression in this assignment so it sets longest to
be one of the longest words in listOfWords, ignoring vowels.  One correct
answer is 'students'. '''

longest = max(a_list, key=len)
                                                             
#print(longest)




