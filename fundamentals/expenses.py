import random

expenses = []

autogenerate = input("Would you like to autogenerate a list? (y/n): ")

if autogenerate == "y":
    expenses = [round(random.uniform(0, 100), 2) for _ in range(7)]
elif autogenerate == "n":
    expenses = [float(input("Enter an expense amount: ")) for _ in range(7)]
else:
    print("Enter 'y' or 'n'")
    exit()

total = round(sum(expenses), 2)
print("Expenses:", ", ".join([f"${expense:.2f}" for expense in expenses]))
print(f"You spent: ${total:.2f}")
