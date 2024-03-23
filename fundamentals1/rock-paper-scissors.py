import random

computer = random.choice(['rock', 'paper', 'scissors'])
user = input('Rock, paper, or scissors? ')  # user input
if user == computer:
    print('Tie!')
elif (user == 'rock' and computer == 'paper') or (user == 'paper' and computer == 'scissors') or (user == 'scissors' and computer == 'rock'):
    print('You lose!')
else:
    print('You win!')
    
print('Computer:', computer)
print('User:', user)

# Output
# Rock, paper, or scissors? rock
# You lose!
# Computer: paper
# User: rock