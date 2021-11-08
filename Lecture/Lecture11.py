from math import pi, sqrt
from functools import reduce
import string

def read_file():
    filename = input("Name of file: ")
    myfile = open(filename, "r") # "r" is for read
    contents = myfile.read()
    myfile.close()
    return contents

def write_file(string):
    filename = input("Name of file: ")
    myfile = open(filename, "w") # "w" is for write
    myfile.write(string)
    myfile.close()

def rf_2(filename):
    with open(filename, "r") as f:
        return f.read()

def rf_3(filename):
    with open(filename, "r") as f:
        return f.readlines()

def rf_4(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line.strip())

def splitexample():
    string = "a-b-c"
    return string.split("-")

def read_preferences(filename):
    dic = {}
    with open(filename, "r") as f:
        for line in f:
            [username, singers] = line.strip().split(":")
            singersList = singers.split(",")
            dic[username] = singersList
    return dic
