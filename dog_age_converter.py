"""
Dog Age Converter
1. Welcome the user
2. Ask for the dog's name
3. Ask for the dog's age
4. Convert dog years to human years and show the result
"""

# Welcome message
print("Welcome to the Dog Age Converter!")

# Ask for the dog's name
dog_name = input("What is your dog's name? ")

# Ask for the dog's age (input() gives a string, so we cast it to an int)
dog_age = int(input(f"How old is {dog_name} in dog years? "))

# 1 dog year = 7 human years
human_age = dog_age * 7

# Show the result with an f-string
print(f"If {dog_name} were a human, {dog_name} would be {human_age} years old!")
