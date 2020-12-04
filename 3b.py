f = open('input/3a_input.txt', 'r')
lines = f.readlines()
f.close()

lines = [line.strip() for line in lines if len(line.strip()) > 0]
is_tree = [[v=='#' for v in line] for line in lines]
num_rows = len(lines)
num_cols = len(lines[0])

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

final_prod = 1

for (dcol, drow) in slopes:
    row_i = drow
    col_i = dcol
    trees_encountered = 0
    while row_i < num_rows:
        if is_tree[row_i][col_i]:
            trees_encountered += 1
        row_i += drow
        col_i = (col_i + dcol) % num_cols

    print(trees_encountered)
    final_prod *= trees_encountered

print(final_prod)