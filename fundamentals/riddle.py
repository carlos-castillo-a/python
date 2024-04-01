# If you flip a coun 100 times, it gives you a sequence of heads (H) and tails (T).
# For each "HH" in the sequence of flips, Alice gets a point.
# For each "HT", Bob gets a point. For example, the sequence:
# "THHHT"
# Would give Alice two points and Bob one.
# Who is most likely to win?

import random
import re

# Define the game
def game(sequence_length):
    flips = "".join([random.choice(['H', 'T']) for _ in range(sequence_length)])
    a_points = len(re.findall('(?=(HH))', flips))
    b_points = len(re.findall('(?=(HT))', flips))
    
    return a_points, b_points


# Simluate the flips
def simulate(n_games, sequence_length):
    a_win, b_win, tie, games_played = 0, 0, 0, 0
    for _ in range(n_games):
        sequence = game(sequence_length)
        games_played += 1
        if sequence[0] > sequence [1]:
            a_win += 1
        elif sequence[1] > sequence [0]:
            b_win += 1
        else:
            tie += 1
    
    a_percentage = f"{round((a_win/games_played)*100, 2)}%"
    b_percentage = f"{round((b_win/games_played)*100, 2)}%"
    tie_percentage = f"{round((tie/games_played)*100, 2)}%"
    
    if a_win > b_win:
        winner = f"Alice wins more often with {a_percentage} of all flips."
    elif a_win < b_win:
        winner = f"Bob wins more often with {b_percentage} of all flips."
    else:
        winner = "It's a tie."

    percentage = f"Alice wins {a_percentage}, Bob Wins {b_percentage}, and ties occur {tie_percentage} of the time"
    return(f"\n{winner}\nStats: {percentage}]\n")

n_games = 50000
sequence_length = 100

print(simulate(n_games, sequence_length))