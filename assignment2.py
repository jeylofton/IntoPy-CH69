"""
Assignment 2 - Simple Python Scripts
Jey Lofton

PART 1: LISTS
- Creating a list
- Accessing items by index
- Replacing values
- Removing items (by value and by index)
- Printing the list and its length

PART 2: DICTIONARIES
- Creating a dictionary with key:value pairs
- Accessing values using keys
- Adding new keys
- Updating existing values
- Removing keys
- Printing the dictionary and its length after every step
"""

# -------------------------------
#  PART 1: LISTS
# -------------------------------

print("----- PART 1: LISTS -----")

# Creating a list
sports = ["basketball", "soccer", "tennis", "boxing", "golf"]
print("My list:", sports)
print("Length:", len(sports))

# Accessing items by index (indexing starts at 0, and -1 is the last item)
print("First item:", sports[0])
print("Third item:", sports[2])
print("Last item:", sports[-1])

# Replacing a value by assigning to its index
sports[1] = "football"
print("After replacing index 1:", sports)
print("Length:", len(sports))

# Removing an item BY VALUE with remove()
sports.remove("golf")
print("After removing 'golf' by value:", sports)
print("Length:", len(sports))

# Removing an item BY INDEX with pop() (pop also hands the item back)
removed = sports.pop(0)
print("Popped item at index 0:", removed)
print("After removing by index:", sports)
print("Length:", len(sports))

# Printing the final list and its length
print("Final list:", sports)
print("Total items:", len(sports))


# -------------------------------
#  PART 2: DICTIONARIES
# -------------------------------

print()
print("----- PART 2: DICTIONARIES -----")

# Creating a dictionary with key:value pairs.
# A list uses positions, but a dictionary uses names (keys) to find values.
car = {
    "make": "Kia",
    "model": "Carens",
    "year": 2026,
    "color": "black"
}
print("My dictionary:", car)
print("Length:", len(car))

# Accessing values using keys (square brackets, but with a key instead of an index)
print("Make:", car["make"])
print("Year:", car["year"])

# Adding a new key - assigning to a key that does not exist yet creates it
car["owner"] = "Jey"
print("After adding 'owner':", car)
print("Length:", len(car))

# Updating an existing value - assigning to a key that already exists overwrites it
car["color"] = "red"
print("After updating 'color':", car)
print("Length:", len(car))

# Removing a key with pop() (it hands the value back)
removed_value = car.pop("year")
print("Removed value:", removed_value)
print("After removing 'year':", car)
print("Length:", len(car))

# Printing the final dictionary and its length
print("Final dictionary:", car)
print("Total keys:", len(car))
