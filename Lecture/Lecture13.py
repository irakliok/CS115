from math import pi, sqrt
from functools import reduce
import string

class Person:
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age

    #print function
    def printname(self):
        print(self.firstname, self.lastname)
    #Override string
    def __str__(self):
        return self.firstname + " " + self.lastname

    
class Student(Person):
    def __init__(self, fname, lname, age):
        Person.__init__(self, fname, lname, age)
        self.age = age

    def asleep(self, time):
        return 3 <= time <= 11

    def __str__(self):
        return Person.__str__(self) + ","  + str(self.age) + " years old"

def test():
    me = Student("Irakli", "Okruashvili", 21)
    print(me)
