# Python Fundamentals

![header](../../docs/header-01.png)

These notes are like a beginner's guide to Python, a programming language. We'll cover the very basics, such as different kinds of information Python can understand, how to make choices in your code, how to ask for input and show output, how to organize data in lists, and how to repeat actions with loops. Think of this as your go-to cheat sheet if you're just starting or need a quick reminder.

> _Enhanced with ChatGPT-4 AI_

### What's Inside
- [Types of Information (Data Types)](#types-of-information-data-types)
- [Making Choices (Conditionals)](#making-choices-conditionals)
  - [Trying Things Out (Interactive Shell)](#trying-things-out-interactive-shell)
  - [Asking and Telling (Input & Output)](#asking-and-telling-input--output)
- [Keeping Things in Order (Lists)](#keeping-things-in-order-lists)
- [Do It Again (Loops)](#do-it-again-loops)

## Types of Information (Data Types)
Python is smart! It guesses what type of info you're working with:
- `int` (like `-1`, `0`, `42`): Whole numbers.
- `float` (like `-2.718`, `0.0`, `3.14`): Numbers with decimal points.
- `bool` (just `True` or `False`): Yes or no kind of info.
- `str`: Text, like words or sentences, wrapped in quotes (`'hello'` or `"world"`).

## Making Choices (Conditionals)
Sometimes, you need your code to choose what to do next:
- Use `if`, `elif` (which means "else if"), and `else` to guide those choices.
- Python uses special checks to help make decisions, like `<` (is less than), `==` (is the same as), and `!=` (is not the same as).
- You can also mix these checks with words like `and`, `or`, and `not` to make more complex choices.

### Trying Things Out (Interactive Shell)
The interactive shell is like a playground to test your code quickly:
- You type your code and see what happens right away.
- It's super useful for experimenting or solving quick problems.
- Here's what it looks like when you play with numbers:
```bash
python3
>>> amount = 100
>>> tax = 0.0625
>>> total = amount + amount * tax
>>> print(total)
106.25
```

### Asking and Telling (Input & Output)
- To show information, use `print()`.
- To get information from someone using your program, use `input()`.
- Like this:
```python
# This script might be saved as input.py
name = input("What's your name? ")
print("Hello,", name)
```

## Keeping Things in Order (Lists)
Lists help you keep track of items in order:
- You can have a list of numbers (`[1, 2, 3]`), words (`['hello', 'world']`), or even a mix of things (`[1, 'two', 3.0]`).
- Lists start counting at 0, not 1. So, the first item is at position 0.
- You can add to a list with `.append()`, remove with `.remove()`, or use `del` to delete something specific.
- Like this:
```python
friends = ["Alice", "Bob", "Charlie"]
friends.append("Dana")  # Now Dana is added to the end
friends.remove("Bob")   # Bye, Bob
del friends[0]          # Alice is also gone now
# Now the list is just ["Charlie", "Dana"]
```

## Do It Again (Loops)
Loops let you repeat actions without writing the same code over and over:
- A `for` loop goes through items one by one.
- You can tell it to go through each item in a list, for example.
- It's like saying, "For each friend in my list of friends, do this."
- Like this:
```python
for friend in ["Alice", "Bob", "Charlie"]:
    print("Hi", friend)
# It says hi to each friend.
```
