import random

n = 0

for exp in range(10000):
    sequence = []

    # Create a list of 100 'heads' or 'tails' value
    for i in range(100):
        if random.randint(0, 1) == 0:
            sequence.append('H')
        else:
            sequence.append('T')
        #print(sequence)
        #print(sequence[i:i+6])
    
    # Check if there is a streak of 6 heads or tails in a row
    for j in range(len(sequence) -5):
        if sequence[j:j+6] == ['H'] * 6 or sequence[j:j+6] == ['T'] * 6:
            n += 1
            break

print('Chance of streak: %s%%' % (n / 100))