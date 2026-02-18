import random

print('Guess the coin toss! Enter 0 (heads) or 1 (tails):')
guess = ''
toss = random.randint(0, 1)  # 0 is tails, 1 is heads

while guess not in(0, 1):
    guess = int(input('Enter 0 (tails) or 1 (heads): '))
 
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = int(input())
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')