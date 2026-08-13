"""
Tuples are just like lists- But!!! They are IMMUTABLE (can't change after creating)
create with ()
"""

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

#accessing item
print(my_tuple[1])
print(my_tuple[-2])

# checking if a item exists
if "apple" in my_tuple:
    print("yes")

# length of a tuple
print(len(my_tuple))

#single item tuple
single = ("water",)
print(type(single))

not_tuple=("water")
print(type(not_tuple))

#nested tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
combined = (tuple1, tuple2)
print(combined)

# Count and Index
# Because tuples are immutable, they dont have methonds like remove or add
letters = ("a", "b", "a", "c", "a")
print(letters.count("a"))  # how many times "a" appears
print(letters.index("c"))  # the index where "c" first appears

# Tuple Unpacking
# You can "unpack" a tuple's items directly into separate variables.
coordinates = (10, 20)
x, y = coordinates
print(x)
print(y)

person = ("leo", 27, "Computer science")
name, age, major = person
print(f"{name} is {age} years old and studies {major}")
