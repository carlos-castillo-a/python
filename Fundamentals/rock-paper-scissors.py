import random

computer = random.choice(['rock', 'paper', 'scissors'])
user = input('Rock, paper, or scissors? ')  # user input
if user == computer:
    print('Tie!')
elif user == 'rock' and computer == 'paper':
    print('You lose!')
elif user == 'rock' and computer == 'scissors':
    print('You win!')
elif user == 'paper' and computer == 'rock':
    print('You win!')
elif user == 'paper' and computer == 'scissors':
    print('You lose!')
elif user == 'scissors' and computer == 'rock':
    print('You lose!')
elif user == 'scissors' and computer == 'paper':
    print('You win!')
else:
    print('Huh?')
    
print('Computer:', computer)
print('User:', user)

# Output
# Rock, paper, or scissors? rock
# You lose!
# Computer: paper
# User: rock