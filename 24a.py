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