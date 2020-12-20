from copy import deepcopy

f = open('input/20a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

tiles_d = dict()
edges_d = dict()

for i in range(len(lines)):
    line = lines[i]
    if line.startswith('Tile'):
        current_tile_num = int(line.strip(':').split(' ')[1])
        tile = []
    elif len(line) == 0 or i == len(lines)-1:
        if i == len(lines)-1:
            tile.append(line)
        # between tiles
        print(current_tile_num)
        print(tile)

        top_edge = tile[0]
        top_edge_r = top_edge[::-1]

        bottom_edge = tile[-1]
        bottom_edge_r = bottom_edge[::-1]

        left_edge = "".join([line[0] for line in tile])
        left_edge_r = left_edge[::-1]

        right_edge = "".join([line[-1] for line in tile])
        right_edge_r = right_edge[::-1]

        tiles_d[current_tile_num] = dict()

        for edge in [
            top_edge, top_edge_r,
            bottom_edge, bottom_edge_r,
            left_edge, left_edge_r,
            right_edge, right_edge_r]:

            tiles_d[current_tile_num][edge] = None # placeholder

            if edge not in edges_d:
                edges_d[edge] = [current_tile_num]
            else:
                edges_d[edge].append(current_tile_num)
    else:
        tile.append(line)

for edge in edges_d:
    for tile_num in edges_d[edge]:
        tiles_d[tile_num][edge] = len(edges_d[edge])

corner_candidates = []
for k in tiles_d:
    counts = sorted([tiles_d[k][edge] for edge in tiles_d[k]])
    if [1, 1, 1, 1] == counts[:4]:
        corner_candidates.append(k)

print(corner_candidates)
prod = 1
for c in corner_candidates:
    prod *= c 
print(f"The result is {prod}")