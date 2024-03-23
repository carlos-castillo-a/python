import random

# If you flip a coun 100 times, it gives you a sequence of heads (H) and tails (T).
# For each "HH" in the sequence of flips, Alice gets a point.
# For each "HT", Bob gets a point. For example, the sequence:
# "THHHT"
# Would give Alice two points and Bob one.
# Who is most likely to win?

def game(sequence_length):
    flips = "".join([random.choice(['H', 'T']) for _ in range(sequence_length)])
    a_points = flips.count('HH')
    b_points = flips.count('HT')
    
    return a_points, b_points

def simulate(n_games, sequence_length):
    a_win, b_win, tie = 0, 0, 0
    for _ in range(n_games):
        sequence = game(sequence_length)
        if sequence[0] > sequence[1]:
            a_win += 1
        elif sequence[1] > sequence[0]:
            b_win += 1
        else:
            tie += 1
    
    a_percentage = round((a_win / n_games) * 100, 2)
    b_percentage = round((b_win / n_games) * 100, 2)
    tie_percentage = round((tie / n_games) * 100, 2)
    
    if a_win > b_win:
        winner = f"Alice wins more often with {a_percentage}% of all flips."
    elif a_win < b_win:
        winner = f"Bob wins more often with {b_percentage}% of all flips."
    else:
        winner = "It's a tie."

    percentage = f"Alice wins {a_percentage}%, Bob wins {b_percentage}%, and ties occur {tie_percentage}% of the time."
    return f"Winner: \n{winner}\nStats: {percentage}\n"

n_games = 10000
sequence_length = 100

print(simulate(n_games, sequence_length))
