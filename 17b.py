from copy import deepcopy

f = open('input/17a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

space_d = dict()
for y in range(len(lines)):
    for x in range(len(lines[0])):
        space_d[(x, y, 0, 0)] = lines[y][x]

def get_neighbors(p):
    (x, y, z, w) = p
    result = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                for dw in [-1, 0, 1]:
                    if not (dx == 0 and dy == 0 and dz == 0 and dw == 0):
                        result.append((x + dx, y + dy, z + dz, w + dw))
    return result

neighbors_d = dict()
NUM_ROUNDS = 6
for r in range(NUM_ROUNDS):
    updated_d = deepcopy(space_d)
    # First add neighbors to the space
    for k in space_d:
        try:
            neighbors = neighbors_d[k]
        except KeyError:
            neighbors = get_neighbors(k)
            neighbors_d[k] = neighbors
        for n in neighbors:
            if n not in space_d:
                updated_d[n] = '.' # inactive by default
    space_d = deepcopy(updated_d)
    updated_d = deepcopy(space_d)
    for k in space_d:
        try:
            neighbors = neighbors_d[k]
        except KeyError:
            neighbors = get_neighbors(k)
            neighbors_d[k] = neighbors
        num_active = sum([n in space_d and space_d[n] == '#' for n in neighbors])
        if space_d[k] == '#':
            if (num_active == 2 or num_active == 3):
                updated_d[k] = '#'
            else:
                updated_d[k] = '.'
        else:
            if num_active == 3:
                updated_d[k] = '#'
            else:
                updated_d[k] = '.'
    space_d = deepcopy(updated_d)
    num_active_end_round = sum([space_d[k] == '#' for k in space_d])
    print(f"Num active after round {r}: {num_active_end_round}")

