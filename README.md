# Dog Age Converter

A small Python program that asks for your dog's name and age, then tells you how old
your dog would be in human years.

**Run it:**

```bash
python3 dog_age_converter.py
```

**Example:**

```
Welcome to the Dog Age Converter!
What is your dog's name? Buddy
How old is Buddy in dog years? 5
If Buddy were a human, Buddy would be 35 years old!
```

## Steps I Took

**1. Printed a welcome message**
Used `print()` to greet the user, the same way I started in `intro.py`.

**2. Asked for the dog's name and saved it in a variable**
Used the `input()` function and stored the answer in `dog_name`, like the
`user_name = input("Enter Your Name: ")` example in `intro.py`.

**3. Asked for the dog's age and cast it to an integer**
`input()` always returns a string, so I wrapped it in `int()` to get a number I could
do math with. This is the same casting idea I practiced in `intro.py` with
`int(input("Enter your age: "))`.

**4. Did the math with an arithmetic operator**
Used the multiplication operator `*` from `operation.py` to multiply the dog's age by 7,
since 1 dog year is about 7 human years, and saved it in `human_age`.

**5. Printed the result with an f-string**
Used an f-string so I could drop `{dog_name}` and `{human_age}` straight into the
sentence, instead of concatenating with `+` and `str()`.

## What I Practiced

- `print()` for output
- Variables to hold the name, age, and result
- `input()` for user input
- Casting with `int()` because `input()` returns a string
- Arithmetic operators (`*`) from `operation.py`
- f-strings for clean output
- Comments and a multi-line docstring at the top to describe the program
