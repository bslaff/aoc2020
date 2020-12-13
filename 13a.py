import math

f = open('input/13a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

earliest = int(lines[0])
candidates = [int(x) for x in lines[1].split(',') if x != 'x']

print(f"Candidates {candidates}")

lowest_id = None
lowest_wait = None

for c in candidates:
    wait = c - (earliest % c)
    if lowest_id is None:
        lowest_wait = wait
        lowest_id = c
    elif wait < lowest_wait:
        lowest_wait = wait
        lowest_id = c

print(f"Lowst_id {lowest_id}, Lowest wait {lowest_wait}, multiplied {lowest_id * lowest_wait}")
