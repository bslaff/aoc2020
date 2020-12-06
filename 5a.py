f = open('input/5a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

seat_ids = []

for line in lines:
    row_part = line[:7]
    col_part = line[7:]

    print(row_part)
    print(col_part)
    
    row_part = row_part.replace('F','0').replace('B','1')[::-1]
    row_part = sum([int(row_part[i])*(2**i) for i in range(len(row_part))])

    col_part = col_part.replace('L','0').replace('R','1')[::-1]
    col_part = sum([int(col_part[i])*(2**i) for i in range(len(col_part))])

    seat_ids.append(row_part * 8 + col_part)

print(max(seat_ids))
