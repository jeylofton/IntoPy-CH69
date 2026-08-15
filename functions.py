"""
A function is a block of code that only runs whne its called.
We can pass data to a function (parameters), and they can return data as a result.

def function_name(parameters):
    Code block (indented)
    perform actions using the parameters
    returns value # optional
"""

# Simple function without parameter

def my_function():
    print("This is my function")

my_function()

# Function with parameters
# Parameters allow you to pass information into a functions
def print_full_name(fname, lname):
    print(f"The name is : {fname} {lname}")

print_full_name("Jey", "Lofton")

# Function that returns values
# Instead of the printing, functions can send back (return) 

def print_full_name(fname, lname):
    return f"{fname} {lname}"

full_name = print_full_name("Jey", "Lofton")
print(full_name)

# Functions with default parameters
# A default parameters means the function will use that value
# if no argument is provided when calling the function.

def greet(name="Student"):
    print(f"Hello, {name}! Welcome to class.")

greet()

greet("Jey")