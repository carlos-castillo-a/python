import random

expenses = []

autogenerate = input("Would you like to autogenerate a list? (y/n): ")

if autogenerate == "y":
    for i in range(7):
        expense = round(random.uniform(0, 100), 2)
        expenses.append(expense)
    total = round(sum(expenses), 2)
    print("Expenses: ", end="")
    for index, expense in enumerate(expenses):
        if index == len(expenses) - 1:
            print(f"${expense:.2f}", end="")
        else:
            print(f"${expense:.2f}", end=", ")
    print()
    print(f"You spent: ${total:.2f}")
elif autogenerate == "n":
    for _ in range(7):
        expense = float(input("Enter an expense amount: "))
        expenses.append(expense)
    total = round(sum(expenses), 2)
    print(f"You spent: ${total}")
else:
    print("Enter 'y' or 'n'")
