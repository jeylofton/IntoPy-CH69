print("Hello world from Python!")
print(2)
print(5+3)
print(True)

# Single Line comments
"""This a note"""

#variable and Concatenation
name ="Jey"
age = 35
print(name, age)

first_name = "Jey"
last_name = "Lofton"
age = 35

print("My name is " + name + " I am " + str(age) + " years old")

animal = "dog"
name = "Paul"
age = 7
state = "Florida"
birth = "January 23, 1999"
person = "Beverly"
fruit = "Banana"
number = 5
car = "Kia Carens"
year = 2026

print (person + " had a "  + animal + " named " + name + " She lived in " + state + " and she was born on " + birth +  person + " drives a " + str(year) + car + ". Her " + animal + " loves " + str(number) + fruit)

#F-String
print(f"A {person} had a {animal} named {name} she lived in the state of {state} and she was born on {birth} she drives a {year} {car} Her {animal} love to eat {number} {fruit} for breakfast")

# User Input Function
user_name = input("Enter Your Name: ")
print(f"Hello, {user_name}!")

#input() always returns a string
print(type(input("Enter your name: ")))

# new_age = in

"""
Pizza Calculator
1. Ask how many slices of pizza and how many people.
2. Use math operators to calculate slices per person. (divide /)
3. Show the results with an f-string
"""

# SHORTCUTS:
# save file: ctrl + s windows| cmd+s mac
# up on arrow key gose to previous commands

# SINGLE LINE Comments

"""
Multi line make sure to use 3 quotes before and after 
"""
'''
this works too with single quotes
'''

# Variables and Concatenation
name = "Leo"
age = 28
print(name, age)

# cant concatinate an interger with a string
print("My name is " + name + " an I am " + str(age) + " years old.")


"""
Write a short story using variables.
1. Declare and initialize 5 variables (strings and numbers)
2. use print() and concatenation to tell a story
3. run the program in terminal
"""

place = "Disneyland"
activity = "riding the rollercoaster"
members = 5
print("The last time I went to " + place + ", i had a greate time " + activity + " with " + str(members) + " friends.")

# F-String
print(f"The last time I went to {place}, and i had a great time {activity}; with all {members} friends.")

# Multi-line f-string
print(f"""The last time I went to {place}, and i had a great time 
{activity}; with all {members}

friends.""")

# Type Function
print(type(name))  # string
print(type(age))   # int
print(type(False)) # bool

# Casting (changing data types)
print(20 + int("20"))
print(20 + age)

# User Input Function
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")

# input() always returns a sting
# print(type(input("Enter your name: ")))

# new_age = int(input("Enter your age: "))
# print(age + new_age)

"""
Pizza Calculator
1. Ask how many slices of pizza and how many people.
2. Use math operators to calculate variable = slices per person. (divide /)
3. Show the results with an f-string
"""

slices = int(input("How many silce of pizza you you want? "))
people = int(input("How many people are sharing the pizza? "))

slice_per_person = slices / people

print(f"Each person gets {slice_per_person} slices of pizza")