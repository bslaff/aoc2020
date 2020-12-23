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

games_winners_d = dict()

def play_game(p1_cards, p2_cards):

    rounds_cards = set()

    # Play rounds
    while True:
        both_cards = (tuple(p1_cards), tuple(p2_cards))
        if both_cards in games_winners_d:
            return games_winners_d[both_cards]

        if both_cards in rounds_cards:
            return (1, p1_cards) # player 1 wins the GAME
        else:
            rounds_cards.add(both_cards)

        p1 = p1_cards.popleft()
        p2 = p2_cards.popleft()

        if len(p1_cards) >= p1 and len(p2_cards) >= p2:
            # play a new GAME of recursive combat to determine the ROUND winner!
            (round_winner, winners_cards) = play_game(deque(list(p1_cards)[:p1]), deque(list(p2_cards)[:p2]))

        else:
            # winner of the ROUND is the player with the higher-value card
            if p1 > p2:
                round_winner = 1
            elif p2 > p1:
                round_winner = 2

        if round_winner == 1:
            p1_cards.append(p1)
            p1_cards.append(p2)
        elif round_winner == 2:
            p2_cards.append(p2)
            p2_cards.append(p1)

        if len(p1_cards) == 0 or len(p2_cards) == 0:
            if len(p1_cards) == 0:
                games_winners_d[both_cards] = (2, p2_cards)
                return (2, p2_cards)
            else:
                games_winners_d[both_cards] = (1, p1_cards)
                return (1, p1_cards)


(round_winner, winners_cards) = play_game(deepcopy(p1_cards), deepcopy(p2_cards))

print()
print("==Post-game results==")
print(f"Winner Player {round_winner}'s deck: {winners_cards}")

cards = list(winners_cards)[::-1]
score = sum([(i+1)*cards[i] for i in range(len(cards))])
print(f"The winner's score is {score}")