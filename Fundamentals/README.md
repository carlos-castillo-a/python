# Notes

## Conditionals
- There are six *comparators* in Python that are relevant to an if/then statement
	- `<` : less than
	- `<=` : less than or equal to
	- `==` : equal
	- `>=` greater than or equal to
	- `>` greater than
	- `!=` : not equal to

### Weather
Run [weather.py](weather.py) for example:
```bash
$ python3 weather.py 
It's too hot! > 80: 
```

### Rock ,Paper, Scissors
- Using `if/else` statements allow you to create a check to see if something is true or not and create custom outputs depending on results
- The [Python Standard Library](https://docs.python.org/3/library/index.html) contains built in functions that can me imported, in this case the [random](https://docs.python.org/3/library/random.html) function

Run [rock-paper-scissors.py](rock-paper-scissors.py) for example:
```bash
$ python3 rock-paper-scissors.py
rock, paper, or scissors? rock
You lose!
Computer: paper
User: rock
```

## Data Types
- Python assumes the type of variable based on the assigned value
	- `int`
	- `float`
	- `bool`
	- `string`

### Tax Calculator
- **Interactive Shell**
	- Immediate response, not easy to edit
	- Used in a terminal
```bash
python3
Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> amount = 100
>>> tax = 0.0625
>>> total = amount + amount*tax
>>> total
106.25
>>>
```

- **Python Script**
	-  Files with the `.py` type
    -  Example: [tax.py](tax.py)
    - Running from command line:
```bash
$ python3 tax.py 
106.25
```
## Input & Output
- The `print()` function can be "called" to output a value, in this case total
	- This is a built in function of python like many others
- The `input()` function prompts the user for an entry
- Example [input.py](input.py) script:
```bash
$ python3 input.py 
Whats your name?
> Bob
Hello Bob
```

### Age Calculator
The [age-calc.py](age-calc.py) file contains the follwoing:
```python
age = input("How old are you?\n")

# Check if the input can be converted to a float
try:
    age = float(age)
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Convert age to an integer
age = int(age)
decades = age // 10
years = age % 10

print(f"You are {decades} decades and {years} years old.")
```

Output:
```Bash
$ python3 age-calc.py
How old are you?
24.4
You are 2 decades and 4 years old.
```
