# This File will be used as notes for the basics of python
# There is a lot in this file, you should add, subtract, change things as needed to help fully understand the process.
# Mr. Berg will be going over all parts, but will not be grading anything in this file

# types

# str
y = "I love Computer Science!"
print(y)

# numbers
mynum = 47
anothernum = 47.7
print(type(mynum))
print(type(anothernum))

# bools - True, False
flag = True
print(flag)

# lists - can hold a list of items of any type
lane_tech = ["chicago", "high school", 1908, 60618, "addison/western"]
print(lane_tech.reverse())
print(lane_tech)
z = lane_tech.pop()
print(z)


# Indices
print(lane_tech[1])
print(lane_tech[-1])
print(lane_tech[len(lane_tech)-1])

# Slices
print(lane_tech[1:3])
print(lane_tech[:3])
print(lane_tech[1:])
print(lane_tech[:])

# Functions

# defining a function
def hello_world():
    print("hello world")

# calling a function
hello_world()
hello_world()

def add_two(n):
    """Takes a number and returns that number + 2
    
    Args: 
        n - a number
    
    Returns:
        the input number + 2
    """
    return n + 2

print(add_two(5))

assert add_two(5) == 7, "add_two with input 5 test"
assert add_two(-2) == 0, "add_two with input -2 test"
assert add_two(0) == 2, "add_two with input 0 test"

# Loops

# For Loop Template 1
# do something for each item in a list
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

for el in lst:
    print(el)

num_list = [1, 34, 67, 98, 104]

for el in num_list:
    print(el)

s=0

for el in num_list:
    s += el
print(s)

# For Loop Template 2
# do something n times
for i in range(5):
    print("Intro to AI")

# For Loop Template 3
# do something for each item in a list but we care about the index
for r in range(len(lst)):
    if lst[r] == 'b':
        lst[r] = 'c'

print(lst)

# Dictionaries

dict = {"name": "rob", "age": 30}
print(dict["age"])
#key=name, value=rob
#key=age, value=30 

# "key": value, so when ask for key in dict["key"], the value will be printed, hence a dictionary

dict = {"drink": "water"}
print(dict["drink"])

# Random
import random

food = ['pizza', 'carrots', 'eggs']
dinner = random.choice(food)
print(dinner)

#food = name of array/list
#dinner is "function," when you print it it will print out a random food from "food"
#random.choice(array) = what makes it actually randomize
# **also you have to import it!!

# f String
age = 25
print("Mary is" , age , "years old")
#you can use commas when printing things! and it adds spaces for you when you put them there

print(f"Mary is {age} years old")
#can put curly brackets around var and it works, but you need an f in front of the string so you dont have to do anything "crazy"
#f stands for "formatter"