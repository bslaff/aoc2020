from copy import deepcopy

f = open('input/11a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

lines = [list(line) for line in lines]
NUM_ROWS = len(lines)
NUM_COLS = len(lines[0])

def adjacent_indices(row_idx, col_idx, lines):
    idxs = []
    for direction in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, 1), (1, 0), (1, -1)]:
        dr = direction[0]
        dc = direction[1]
        r = row_idx + dr
        c = col_idx + dc
        while r >= 0 and r < NUM_ROWS and c >= 0 and c < NUM_COLS:
            if lines[r][c] != '.':
                idxs.append((r, c))
                break
            r += dr
            c += dc
    return idxs

def count_adjacent_occupied(adjacent, lines):
    return sum([lines[r_idx][c_idx] == '#' for (r_idx, c_idx) in adjacent])

adjacent_idxs =  [[adjacent_indices(r, c, lines) for c in range(NUM_COLS)] for r in range(NUM_ROWS)]

while True:
    num_changes = 0
    original_lines = deepcopy(lines)
    for c in range(NUM_COLS):
        for r in range(NUM_ROWS):
            x = lines[r][c]
            if x == '.':
                continue
            num_adj_occ = count_adjacent_occupied(adjacent_idxs[r][c], original_lines)
            if x == 'L' and num_adj_occ == 0:
                lines[r][c] = '#'
                num_changes += 1
            if x == '#' and num_adj_occ >= 5:
                lines[r][c] = 'L'
                num_changes += 1
    print(f"Num changes: {num_changes}")
    if num_changes == 0:
        break
    original_lines = lines

num_occupied = sum([sum([lines[r_idx][c_idx] == '#' for c_idx in range(NUM_COLS)]) for r_idx in range(NUM_ROWS)])
print(f"Num occupied: {num_occupied}")