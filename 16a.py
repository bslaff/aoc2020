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
for ticket in nearby_tickets:
    for x in ticket:
        if x not in all_allowed:
            rate += x

print(f"The scanning error rate is {rate}")