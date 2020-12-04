f = open('input/3a_input.txt', 'r')
lines = f.readlines()
f.close()

lines = [line.strip() for line in lines if len(line.strip()) > 0]
is_tree = [[v=='#' for v in line] for line in lines]
num_rows = len(lines)
num_cols = len(lines[0])

row_i = 1
col_i = 3
trees_encountered = 0
while row_i < num_rows:
    if is_tree[row_i][col_i]:
        trees_encountered += 1
    row_i += 1
    col_i = (col_i + 3) % num_cols

print(trees_encountered)