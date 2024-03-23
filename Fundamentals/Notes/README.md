# Python Fundamentals

![header](../../docs/header-01.png)

These notes provide a comprehensive overview of fundamental Python programming concepts, tailored for both beginners looking to grasp the basics and for seasoned programmers seeking a quick reference. Covered topics include data types, conditional statements, input/output operations, lists, and loops, enhanced with practical examples to facilitate a deeper understanding of the language.

> _Enhanced with ChatGPT-4 AI_

### Table of Contents
- [Data Types](#data-types)
- [Conditionals](#conditionals)
  - [Interactive Shell](#interactive-shell)
  - [Input & Output](#input--output)
- [Lists](#lists)
- [Loops](#loops)

## Data Types
Python dynamically infers the type of a variable based on the value assigned to it. The primary data types are:
- `int`: Integer, a whole number without a fractional component (examples: `-3`, `0`, `42`).
- `float`: Floating-point number, a number with a fractional part (examples: `-2.718`, `0.0`, `3.14`).
- `bool`: Boolean, represents truth values (`True` or `False`).
- `str`: String, a sequence of characters enclosed in single (`'...'`) or double (`"..."`) quotes.

## Conditionals
Conditional statements enable the execution of different blocks of code based on specified conditions:
- Use `if`, `elif` (else if), and `else` for creating conditional branches.
- Python supports six comparators for condition testing:
    - `<`: Less than
    - `<=`: Less than or equal to
    - `==`: Equal to
    - `>=`: Greater than or equal to
    - `>`: Greater than
    - `!=`: Not equal to
- Combine multiple conditions using logical operators: `and`, `or`, and `not`.

### Interactive Shell
The Python interactive shell offers an immediate way to execute and test Python code:
- Accessible through a terminal or command prompt.
- Example session demonstrating variable assignment and arithmetic operations:
```bash
python3
Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) on darwin
>>> amount = 100
>>> tax = 0.0625
>>> total = amount + amount * tax
>>> print(total)
106.25
```

### Input & Output
- The `print()` function outputs values to the console.
- The `input()` function captures user input as a string.
- Example usage within a script named [input.py](../input.py).

## Lists
Lists are versatile data structures for storing ordered collections of items, which can be of any type:
- Examples of lists include an empty list (`empty = []`), a list of numbers (`nums = [1, 5, 10]`), strings (`words = ['hello', 'world']`), mixed types (`mixed = [3, 'pi', 3.14]`), and nested lists (`nested = [['a', 'b', 'c'], ['1', '2', '3']]`).
- Lists use zero-based indexing. To access the _n_th item, use the index `[n-1]`.
- Modify lists with methods like `.append()` for adding items and `.remove()` for removing items. Alternatively, use `del` with an index for removal.
```python
acronyms = ["LOL", "IDK", "SMH", "TBH"]
acronyms.append("JK")  # Adds "JK" to the end of the list
acronyms.remove("SMH") # Removes "SMH" from the list
del acronyms[2]        # Removes the third item from the list
# Resulting list: ["LOL", "IDK", "TBH", "JK"]
```

### Loops
Loops are used for iterating over a sequence, like a list, and executing a block of code multiple times:
- A `for` loop processes each item in a sequence in turn.
- Syntax includes `for`, a loop variable, `in`, the sequence, and a colon `:`.
- Use the `range()` function to iterate over a sequence of numbers.
```python
for item in ["LOL", "IDK", "TBH"]:
    print(item)
# This loop prints each acronym in the list.
```
