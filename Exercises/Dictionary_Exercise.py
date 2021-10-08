#!/usr/bin/env python
# coding: utf-8

# In[1]:


grades = {
    "John": [98, 79, 100],
    "Mary": [56, 79, 28],
    "Eve": [68, 45, 88],
    "Alice": [80, 99, 65],
    "Bob": [87, 90, 95]
}


# In[2]:


def listStudents(dic):
    """Given a dictionary with (student name,list of grades) as key-value pairs, 
       return the list of students names"""
    return list(dic.keys())


# In[3]:


print(listStudents(grades))


# In[4]:


#Write a lambda function that takes a list as an input and returns the mean of the lists elements
list_average = lambda x : round(sum(x)/len(x),3)


# In[5]:


def searchStudent(dic, name):
    """Given a dictionary with (student name,list of grades) as key-value pairs and a student name,
       return a tuple containing the student name and average grade for that student"""
    if name in dic:
        return (name, list_average(dic[name]))
    else:
        return "Student not found in this class"



# In[6]:


print(searchStudent(grades, "John"))


# In[7]:


print(searchStudent(grades, "Joe"))


# In[8]:


#print out the class average
def computeIndividualAverage(grades):
    """Given a dictionary with (student name,list of grades) as key-value pairs,
       return a dictionary containing the student name and average grade as key-value pairs"""
    return dict(map(lambda x: (x[0], list_average(x[1])), grades.items()))


# In[9]:


print(computeIndividualAverage(grades))


# In[10]:


def getSubsetStudents(grades, threshold):
    """Given a dictionary with (student name,list of grades) as key-value pairs and a threshold,
       return a list of tuples containing the names and the average grades of students with average grade greater than the threshold"""
    return dict(map(lambda x: (x[0], list_average(x[1]))


# In[11]:


print("Students getting A are: ", getSubsetStudents(grades, 90))

