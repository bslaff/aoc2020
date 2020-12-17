from copy import deepcopy

f = open('input/16a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

criteria = dict()
your_ticket = None
nearby_tickets = []

i = 0
while not len(lines[i]) == 0:
    line = lines[i].split(':')
    ranges = [[v.split('-')[0], v.split('-')[1]] for v in line[1].strip().split(' or ')]
    ranges = [set(list(range(int(v[0]), int(v[1]) + 1))) for v in ranges]
    allowed = set().union(*ranges)
    criteria[line[0].strip()] = allowed
    i += 1

all_allowed = set().union(*list(criteria.values()))

i += 2
your_ticket = [int(v) for v in lines[i].split(',')]

i += 3
while i < len(lines):
    nearby_tickets.append([int(v) for v in lines[i].split(',')])
    i += 1

rate = 0
copied_nearby_tickets = deepcopy(nearby_tickets)
for ticket in copied_nearby_tickets:
    for x in ticket:
        if x not in all_allowed:
            nearby_tickets.remove(ticket)

print(f"Original ticket count: {len(copied_nearby_tickets)}")

print(f"Valid ticket count: {len(nearby_tickets)}")

valid_tickets = nearby_tickets + [your_ticket]
by_position = [set([ticket[i] for ticket in valid_tickets]) for i in range(len(your_ticket))]

print(by_position)

assignment_d = dict()
for field in criteria:
    assignment_d[field] = []
for field in criteria:
    for i in range(len(by_position)):
        if by_position[i].issubset(criteria[field]):
            assignment_d[field].append(i)

for k in assignment_d:
    assignment_d[k] = set(assignment_d[k])

# Probably can do better than N^2 here but this is fast...
while max([len(assignment_d[k]) for k in assignment_d]) > 1:
    for k in assignment_d:
        if len(assignment_d[k]) == 1:
            determined_k = k
            for kk in assignment_d:
                if kk != determined_k:
                    assignment_d[kk] -= assignment_d[determined_k]

for k in assignment_d:
    assignment_d[k] = list(assignment_d[k])[0]

prod = 1
for k in assignment_d:
    if k.startswith('departure'):
        prod *= your_ticket[assignment_d[k]]

print(f"The result is {prod}")