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

# Output:
# How old are you?
# 35
# You are 3 decades and 5 years old.