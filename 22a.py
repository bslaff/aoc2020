from copy import deepcopy
from collections import deque

f = open('input/22a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

p1_cards = deque()
p2_cards = deque()

idx = 1
while len(lines[idx]) > 0:
    p1_cards.append(int(lines[idx]))
    idx += 1

idx += 2
while lines[idx]:
    p2_cards.append(int(lines[idx]))
    idx += 1
    if idx == len(lines):
        break

# Play rounds
while True:
    print(f"Player 1's deck: {p1_cards}")
    print(f"Player 2's deck: {p2_cards}")
    p1 = p1_cards.popleft()
    p2 = p2_cards.popleft()
    print(f"Player 1 plays: {p1}")
    print(f"Player 2 plays: {p2}")
    if p1 > p2:
        print("Player 1 wins the round!")
        p1_cards.append(p1)
        p1_cards.append(p2)
    elif p2 > p1:
        print("Player 2 wins the round!")
        p2_cards.append(p2)
        p2_cards.append(p1)
    else:
        print("SQUAWK!")
    if len(p1_cards) == 0 or len(p2_cards) == 0:
        if len(p1_cards) == 0:
            winner_cards = p2_cards
        else:
            winner_cards = p1_cards
        break

print()
print("==Post-game results==")
print(f"Player 1's deck: {p1_cards}")
print(f"Player 2's deck: {p2_cards}")

cards = list(winner_cards)[::-1]
score = sum([(i+1)*cards[i] for i in range(len(cards))])
print(f"The winner's score is {score}")



