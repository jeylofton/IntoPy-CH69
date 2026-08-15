"""
A while loop repeats a block of code as long as the condition is True.
BE CAREFUL - if the condition Never becomes False, you'll get an INFINITE loop!

Declare a funtion to allow it to stop.

while condition
"""

count = 1

while count <= 5:
    print("Count is: ", count)
    count += 1

print("-------------------------------------------------------------")

count = 0 # initialize count at 0

while count <= 10:
    print(count)
    count += 1
    if count == 6:
        break

    # using CONTIUNE to SKIP an iteration
count = 0
while count <= 10:
    count += 1
    if count == 6:
        continue
    print(count)

print("-------------------------------------------------------------")

count = 1
while count < 3:
    print(count)
    count += 1
else:
    print("Loop Finished!")

"""
-------------------------------
MINI CHALLENGE: WHILE LOOP
-------------------------------
Guess the Secret Number
1. Create a variable called secret_number
and set it equal to 7.
2. Ask the user to guess the number.
3. Use a while loop to keep asking until
they guess correctly.
4. If the guess is too low:
print "Too low!"
5. If the guess is too high:
print "Too high!"
6. When the user guesses correctly:
print "Correct!"
BONUS:
Count how many guesses the user needed.
"""

# 1. The number the user is trying to find
import random

secret_number = random.randint(1, 10)

# BONUS: a counter that goes up by 1 every time the user guesses
guesses = 0

# 2. Ask for the FIRST guess before the loop starts, so the
#    while condition has something to check
guess = int(input("Guess the secret number (1-10): "))
guesses += 1

# 3. Keep looping as long as the guess is WRONG.
#    != means "not equal to", so the loop stops the moment they get it right.
while guess != secret_number:
    # 4 & 5. Give the user a hint
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    # Ask again INSIDE the loop - this is what makes the condition
    # change, so the loop can eventually end
    guess = int(input("Try again: "))
    guesses += 1

# 6. The loop only exits when the guess is correct
print("Correct!")
print(f"It took you {guesses} guesses.")
