from copy import deepcopy
import numpy as np

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

        top_edge = tile[0]
        top_edge_r = top_edge[::-1]

        bottom_edge = tile[-1]
        bottom_edge_r = bottom_edge[::-1]

        left_edge = "".join([line[0] for line in tile])
        left_edge_r = left_edge[::-1]

        right_edge = "".join([line[-1] for line in tile])
        right_edge_r = right_edge[::-1]

        tiles_d[current_tile_num] = dict()
        tiles_d[current_tile_num]["full tile"] = deepcopy(np.asarray([list(row) for row in tile], dtype=np.unicode_))

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

## Strategy: start with an empty bunch of strings ' '. Replace with tiles by index. Start with one and go one at a time to it's neighbors, calling recursively.
## Only add in a tile if it's not in already. Keep a set to track this.
## Image is 12 x 12 tiles, so 120 x 120
final_image = np.asarray([[' ']*300]*300, dtype=np.unicode_)

START_X = 150
START_Y = 150
tiles_set_down = set()

tile_ids = list(tiles_d.keys())
tile_num = tile_ids[0]

final_image[START_Y:(START_Y + 10),START_X:(START_X + 10)] = tiles_d[tile_num]["full tile"]
tiles_set_down.add(tile_num)

y = START_Y
x = START_X

def set_down_neighbors(x, y, tile_num, tiles_set_down):

    print(f"Set down so far: {len(tiles_set_down)} of 144")

    if len(tiles_set_down) == 144:
        return

    full_tile = final_image[y:(y + 10),x:(x + 10)]

    top_edge = "".join(list(full_tile[0,:]))
    bottom_edge = "".join(list(full_tile[9,:]))
    left_edge = "".join(list(full_tile[:,0]))
    right_edge = "".join(list(full_tile[:,9]))
    
    neighbors = []
    for edge in tiles_d[tile_num]:
        if edge == 'full tile':
            continue
        for tid in edges_d[edge]:
            if tid != tile_num and tid not in neighbors:
                neighbors.append(tid)
    print(f"The neighbors are {neighbors}")
    for neighbor_num in neighbors:
        if neighbor_num == tile_num:
            continue
        if neighbor_num not in tiles_set_down:
            
            # find the matching edge between tile and the neighbor
            full_neighbor = tiles_d[neighbor_num]["full tile"]

            set_neighbor = False
            
            while not set_neighbor:

                neighbor_top_edge = "".join(list(full_neighbor[0,:]))
                neighbor_top_edge_r = neighbor_top_edge[::-1]

                neighbor_bottom_edge = "".join(list(full_neighbor[9,:]))
                neighbor_bottom_edge_r = neighbor_bottom_edge[::-1]

                neighbor_left_edge = "".join(list(full_neighbor[:,0]))
                neighbor_left_edge_r = neighbor_left_edge[::-1]

                neighbor_right_edge = "".join(list(full_neighbor[:,9]))
                neighbor_right_edge_r = neighbor_right_edge[::-1]

                if neighbor_top_edge == bottom_edge or neighbor_top_edge_r == bottom_edge:
                    set_neighbor = True
                    if neighbor_top_edge_r == bottom_edge:
                        full_neighbor = np.fliplr(full_neighbor)
                    neighbor_y = y + 10
                    neighbor_x = x
                elif neighbor_bottom_edge == top_edge or neighbor_bottom_edge_r == top_edge:
                    set_neighbor = True
                    if neighbor_bottom_edge_r == top_edge:
                        full_neighbor = np.fliplr(full_neighbor)
                    neighbor_y = y - 10
                    neighbor_x = x
                elif neighbor_left_edge == right_edge or neighbor_left_edge_r == right_edge:
                    set_neighbor = True
                    if neighbor_left_edge_r == right_edge:
                        full_neighbor = np.flipud(full_neighbor)
                    neighbor_y = y
                    neighbor_x = x + 10
                elif neighbor_right_edge == left_edge or neighbor_right_edge_r == left_edge:
                    set_neighbor = True
                    if neighbor_right_edge_r == left_edge:
                        full_neighbor = np.flipud(full_neighbor)
                    neighbor_y = y
                    neighbor_x = x - 10

                if set_neighbor:
                    print(f"Setting down {neighbor_num} starting at x={neighbor_x} and y={neighbor_y}")
                    final_image[neighbor_y:(neighbor_y + 10),neighbor_x:(neighbor_x + 10)] = full_neighbor
                    tiles_set_down.add(neighbor_num)

                    set_down_neighbors(neighbor_x, neighbor_y, neighbor_num, tiles_set_down)

                full_neighbor = np.rot90(full_neighbor)

set_down_neighbors(x, y, tile_num, tiles_set_down)

where_space = np.where(final_image != ' ')
min_x = min(where_space[0])
max_x = max(where_space[0])
min_y = min(where_space[1])
max_y = max(where_space[1])
final_image = final_image[min_x:(max_x+1), min_y:(max_y+1)] # trimmed white space

row_col_idxs_to_delete = list(np.arange(9, 121, 10)) + list(np.arange(0, 120, 10))
final_image = np.delete(final_image, row_col_idxs_to_delete, axis=0)
final_image = np.delete(final_image, row_col_idxs_to_delete, axis=1)
## Now we have the cropped image with borders all tile removed. Time to find sea monsters.
# np.savetxt("final_image.csv", final_image, delimiter='', fmt="%s")

sea_monster = np.asarray([
    list('                  # '),
    list('#    ##    ##    ###'),
    list(' #  #  #  #  #  #   ')
])
pds = sea_monster == '#'

(XX, YY) = final_image.shape
(SM_XX, SM_YY) = sea_monster.shape

sea_monster_count = 0
while sea_monster_count == 0:
    for x in range(XX - SM_XX):
        for y in range(YY - SM_YY):
            if all([v=='#' for v in final_image[x:(x+SM_XX),y:(y+SM_YY)][pds]]):
                print(f"Sea monster at {x}, {y}")
                sea_monster_count += 1

    sea_monster = np.rot90(sea_monster)
    pds = sea_monster == '#'
    (SM_XX, SM_YY) = sea_monster.shape

print(f"Found {sea_monster_count} monsters")
num_pds = sum([v=='#' for v in final_image.flatten()])
num_pds_in_sm = sum([v=='#' for v in sea_monster.flatten()])

print(f"# in image: {num_pds}")
print(f"# in sea monster: {num_pds_in_sm}")

print(f"The result is {num_pds - sea_monster_count * num_pds_in_sm}")
