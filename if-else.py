"""
Am of-else statement in python is a conditional control structure that lets you
decide which black of code to run depending on whether a condition is True or Falsed.

The if block runs only if the condition evaluates to True
- If the condition is False, the else runs instead
- You can also add elif (else if) blocks to check multiple conditions in a sequence.

if condition:
    - code block runs if the condition is true
elif another_condition:
    - Code block runs if the first conditon is False
    - and this condition is True
else:
    - Code block always runs if non of the above conditions are True
"""

x = 10

if x > 0:
    print("x is a positive number")
elif x == 0:
    print(" x is zero")
else:
    print ("x is negative")

# Short Hand IF statements
if x > 5: print("x is greater than 5")

# Short Hand IF..ELSE
print("Even") if x % 2 == 0 else print ("Odd")

# Nested IF Statements
x = 21
if x > 0:
    if x < 20:
        print("x is a postive numebr less than 20")

# Combining Conditions
age = 19

if age >= 18 and age <= 21:
    print(" You're between 18 and 21 years old")

"""
Mini challenge
Ask the user to enter a number from 0-100 and store it in a variable called "score".
If the score is 90 or above, print "Grade: A".
If the score is between 80-89, print "Grade: B".
If the score is between 70-79, print "Grade: C".
Otherwise, print "Grade: F".
6. Create a variable "passed" — set it to True if score >= 70, otherwise False.
BONUS: If passed is True, print "Congratulations!", otherwise print "Try again!"
"""

score = int(input("Enter a number between 0-100: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

if score >= 70:
    passed = True
else:
    passed = False

if passed:
    print("Congratulations!")
else:
    print("Try again!")
