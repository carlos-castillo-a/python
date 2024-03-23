# Python Fundamentals

These notes delve into the essential concepts of Python programming, aiming to clarify the foundations for beginners and act as a handy guide for those already versed in the language. Topics covered include data types, conditional statements, handling input and output, lists, and looping techniques, all presented with clear examples for better understanding.

> _Enhanced with GPT-4 from OpenAI_

### Table of Contents
- [Interactive Shell](#interactive-shell)
- [Input & Output](#input--output)
- [Data Types](#data-types)
- [Conditionals](#conditionals)
- [Lists](#lists)
- [Loops](#loops)

## Interactive Shell
The Python shell lets you write and test code quickly, directly in the terminal or command prompt. It's great for experiments, though editing code can be tricky.
```bash
python3
Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) on darwin
>>> amount = 100
>>> tax = 0.0625
>>> total = amount + amount * tax
>>> print(total)
106.25
```

## Input & Output
- To show information to the user, use the `print()` function.
- To get information from the user, use `input()`, which waits for the user to type something and press enter.

## Data Types
In Python, the type of a variable (like integer or string) is determined by the value you give it. Here's a quick rundown:
- `int`: For whole numbers without decimals (like `-3`, `0`, or `42`).
- `float`: For numbers with decimals (`-2.718`, `0.0`, `3.14`).
- `bool`: For true/false values.
- `str`: For text, surrounded by quotes (`'like this'` or `"this"`).

## Conditionals
Conditionals let you run different code based on conditions:
- Key words commonly used include `if`, `elif` (which stands for "else if"), and `else`.
- Python supports six comparators for condition testing:
    - `<`: Less than
    - `<=`: Less than or equal to
    - `==`: Equal to
    - `>=`: Greater than or equal to
    - `>`: Greater than
    - `!=`: Not equal to
- You can also use `and`, `or`, and `not` to combine conditions.

## Lists
Lists are used to store collections of items in an ordered way. They can hold anything - numbers, strings, or even other lists:
- Creating a list is as simple as putting items inside square brackets (`[]`), like `nums = [1, 5, 10]` or `words = ['hello', 'world']`.
- Use `.append()` to add an item, `.remove()` to take one out, or `del` with an index if you know where the item is.
```python
acronyms = ["LOL", "IDK", "SMH", "TBH"]
acronyms.append("JK")  # Adds "JK" to the end of the list
acronyms.remove("SMH") # Removes "SMH" from the list
del acronyms[2]        # Removes the third item from the list
# Resulting list: ["LOL", "IDK", "TBH", "JK"]
```

## Loops
Loops repeat actions. For example, a `for` loop goes through items in a list one by one:
- It's written with `for`, followed by a temporary name for the item, then `in`, the list's name, and a colon.
- Use `range()` if you want to repeat something a specific number of times.
```python
for item in ["LOL", "IDK", "TBH"]:
    print(item)
# This loop prints each acronym in the list.
```
