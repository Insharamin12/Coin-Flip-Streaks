import random

numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flips = ''.join(random.choice(['H', 'T']) for _ in range(100))

    # Code that checks if there is a streak of 6 heads or tails in a row.
    if 'HHHHHH' in flips or 'TTTTTT' in flips:
        numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
