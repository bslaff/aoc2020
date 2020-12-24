from copy import deepcopy

f = open('input/24a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

tiles_d = dict()

# x = xa + xb*sqrt(3), with xa, xb rational
# likewise for y
# turns out it didn't need to be even that complicated
for spec in lines:
    (xa, xb, ya, yb) = (0,0,0,0) # start at the ref square
    idx = 0
    while idx < len(spec):

        if spec[idx] == 'e':
            xa += 2
            idx += 1
        elif spec[idx] == 'w':
            xa -= 2
            idx += 1
        elif spec[idx:(idx + 2)] == 'se':
            xa += 1
            yb -= 1
            idx += 2
        elif spec[idx:(idx + 2)] == 'sw':
            xa -= 1
            yb -= 1
            idx += 2
        elif spec[idx:(idx + 2)] == 'ne':
            xa += 1
            yb += 1
            idx += 2
        elif spec[idx:(idx + 2)] == 'nw':
            xa -= 1
            yb += 1
            idx += 2

    coords = (xa, xb, ya, yb)

    if coords not in tiles_d:
        tiles_d[coords] = 'black'
    else:
        if tiles_d[coords] == 'black':
            tiles_d[coords] = 'white'
        else:
            tiles_d[coords] = 'black'

num_black = sum([tiles_d[k] == 'black' for k in tiles_d])

print(f"{num_black} tiles are black")

print(f"There are {len(tiles_d)} tiles identified")

def get_neighbors(coords):

    (xa, xb, ya, yb) = coords

    return [
        (xa + 2, xb, ya, yb),
        (xa - 2, xb, ya, yb),
        (xa + 1, xb, ya, yb - 1),
        (xa - 1, xb, ya, yb - 1),
        (xa + 1, xb, ya, yb + 1),
        (xa - 1, xb, ya, yb + 1)
    ]


NUM_DAYS = 100

neighbors_d = dict()
next_tiles_d = dict()

for k in tiles_d:
    next_tiles_d[k] = tiles_d[k]
    if k not in neighbors_d:
        neighbors = get_neighbors(k)
        neighbors_d[k] = neighbors
        for n in neighbors:
            if n not in tiles_d:
                next_tiles_d[n] = 'white'

tiles_d = deepcopy(next_tiles_d)

for i in range(NUM_DAYS):

    next_tiles_d = dict()

    for k in tiles_d:
        if k not in neighbors_d:
            neighbors_d[k] = get_neighbors(k)

        neighbors = neighbors_d[k]

        for n in neighbors:
            if n not in tiles_d:
                next_tiles_d[n] = 'white'

        num_black = sum([tiles_d[n] == 'black' for n in neighbors if n in tiles_d])
        # print(f"Tile {k} is {tiles_d[k]} and has {num_black} black neighbors")

        if tiles_d[k] == 'black' and (num_black == 0 or num_black > 2):
            next_tiles_d[k] = 'white'
        elif tiles_d[k] == 'white' and num_black == 2:
            next_tiles_d[k] = 'black'
        else:
            next_tiles_d[k] = tiles_d[k]

    tiles_d = deepcopy(next_tiles_d)

    total_num_black = sum([tiles_d[k] == 'black' for k in tiles_d])
    print(f"Day {i+1}: {total_num_black}")