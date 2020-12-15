from math import log2

f = open('input/14a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

def base10_to_binary(num):
    result = [0] * 36
    n = 35
    while n >= 0 and num > 0:
        if log2(num) < n:
            result[35-n] = 0
        else:
            result[35-n] = 1
            num -= 2 ** n
        n -= 1
    return result

def get_mask(line):
    return list(line.split('=')[1].strip())

def apply_mask(num, mask):
    bin_num = base10_to_binary(num)
    for i in range(len(bin_num)):
        if mask[i] != 'X':
            bin_num[i] = int(mask[i])
    return sum([bin_num[i] * (2 ** (35-i)) for i in range(len(bin_num))])

def store_mem(mem, line, mask):
    line = line.split('=')

    num = int(line[1].strip())
    key = int(line[0].strip().strip('mem[').strip(']'))

    mem[key] = apply_mask(num, mask)


mem = dict()
mask = None
for line in lines:
    if line.startswith("mask"):
        mask = get_mask(line)
    else:
        store_mem(mem, line, mask)

total = sum([mem[k] for k in mem])

print(f"The total is {total}")
