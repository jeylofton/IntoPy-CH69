"""
Dictionaries store data in KEY : VALUE pairs
written with curly brackets {}
"""

student = {
    "name": "Leo",
    "age": 24,
    "major": "Computer Science"
}

print(student)

# Accessing Items by KEY
print(student["major"])    
print(student.get("name"))

# Adding New Items
student["graduation_year"] = 2025
print(student)

# Changing Values
student["age"] = 20
print(student)

# Removing Items
student.pop("major") # Remove key "major" and its value
print(student)

# checking if an item exists
if "name" in student:
    print("Key 'name' is in the dictionary")

# Nested Dictionary
studentss = {
    "student1": {"name": "Leo", "age": 22},
    "student2": {"name": "Alex", "age": 25}
}
print(studentss["student2"]["age"])

# Looping Through A Dictoinary
# .key()     -> just the keys
# .values()  -> just the values
# .items()   -> key/value pairs together (most commonly used in loops)

for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(f"{key} : {value}")

# updating multiple keys at once
# update() merges a second dictionary into the first one.
# Existing keys get overwrittn, new kays get added

student.update({"age": 22, "gpa": 3.8})
print(student)

"""
 -------------------------------
MINI CHALLENGE: STUDENT REPORT CARD  MC2.md
-------------------------------
You need to store and analyze a student's grades.

1. Create a dictionary called "report_card" with keys:
    -"name"
    - "subject"
    - "grades" (use a tuple with 3 numbers)
Example: {"name": "Leo", "subject": "Math", "grades": (90, 85, 88)}
2. Print the student's name and subject.
3. Calculate the average of the 3 grades (HINT: use sum() and len()).
4. Add a new key called "average" with the calculated result.
5. If the average is 90 or above → print "Excellent!"
    If between 70 and 89 → print "Good job!"
    Otherwise → print "Needs improvement!"
6. Remove the "subject" key and print the updated dictionary.
"""