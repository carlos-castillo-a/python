# Monty Hall Problem (My bad solution)
# import random
# import click

# x = random.randint(1,3)

# doors = {
#     1: False,
#     2: False,
#     3: False
# }

# doors[x] = True

# door_list = list(doors.keys())
# val_list = list(doors.values())

# prize = []
# not_prize = []

# for key, value in doors.items():
#     if value == True:
#         prize.append(key)
#     else:
#         not_prize.append(key)

# picked_door = int(input("Select door 1, 2, or 3. Enter your answer: "))
# if picked_door > 3 or picked_door < 1:
#     picked_door = input("Please enter a number between 1 and 3: ")
    
# y = random.randint(0,1)

# if picked_door == x:
#     revealed_door = not_prize[y]
#     if y == 0:
#         other_door = not_prize[1]
#     else:
#         other_door = not_prize[0]
# else: 
#     revealed_door = not_prize[1-y]
#     other_door = prize[0]

# switch_choice = click.confirm(f"Good choice! I can now reveal that door {revealed_door} does not have a pize! At this point, would you like to switch to door {other_door}? ", default = False)

# print(f"Okay, now lets see the results!...The prize is behind door: {prize[0]}")

# if switch_choice == True:
#     picked_door = other_door

# if picked_door == x:
#     print("Congratulations, you win!")
# else:
#     print("Looks like you lost!")


# ------------------------------------------------------------ #
#                       GPT-4 Version:                         #
# ------------------------------------------------------------ #

# import random

# def monty_hall():
#     # Initialize doors
#     doors = [False, False, False]
    
#     # Randomly assign a prize behind one door
#     prize_door = random.randint(0, 2)
#     doors[prize_door] = True

#     # Player picks a door
#     picked_door = int(input("Select door 1, 2, or 3. Enter your answer: "))
#     while picked_door not in [1, 2, 3]:
#         picked_door = int(input("Invalid choice! Please select door 1, 2, or 3: "))
#     picked_door -= 1  # Adjust index for 0-based list
    
#     # Host reveals a door that doesn't have a prize and wasn't picked
#     revealed_door = next(i for i in range(3) if i != picked_door and not doors[i])
    
#     # Offer the player to switch doors
#     switch = input(f"Door {revealed_door + 1} does not have the prize. Would you like to switch doors? (yes/no): ")
    
#     if switch.lower() in ['yes', 'y']:
#         picked_door = next(i for i in range(3) if i != picked_door and i != revealed_door)
    
#     # Show results
#     if doors[picked_door]:
#         print(f"Congratulations, you win! The prize was behind door {prize_door + 1}.")
#     else:
#         print(f"You lost! The prize was behind door {prize_door + 1}.")

# if __name__ == "__main__":
#     monty_hall()


### Simulated to show rates
import random

def monty_hall_simulation(num_trials, switch):
    win_count = 0

    for _ in range(num_trials):
        # Initialize doors (False means no prize, True means prize)
        doors = [False, False, False]
        
        # Place the prize behind one random door
        prize_door = random.randint(0, 2)
        doors[prize_door] = True

        # Player randomly picks a door
        picked_door = random.randint(0, 2)
        
        # Host opens a door that has no prize and was not picked
        revealed_door = next(i for i in range(3) if i != picked_door and not doors[i])

        # Player decides whether to switch based on the simulation setup
        if switch:
            picked_door = next(i for i in range(3) if i != picked_door and i != revealed_door)

        # Check if the player wins
        if doors[picked_door]:
            win_count += 1

    return (win_count / num_trials) * 100

def run_simulations(num_trials):
    success_rate_switching = monty_hall_simulation(num_trials, switch=True)
    success_rate_not_switching = monty_hall_simulation(num_trials, switch=False)

    print(f"Switching success rate: {success_rate_switching:.2f}%")
    print(f"Not switching success rate: {success_rate_not_switching:.2f}%")

# Run the simulations
if __name__ == "__main__":
    number_of_trials = 100000  # Change this number to adjust the number of trials
    run_simulations(number_of_trials)
