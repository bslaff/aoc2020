from math import log2

f = open('input/14a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

def base10_to_binary(num, L):
    result = [0] * L
    n = L-1
    while n >= 0 and num > 0:
        if log2(num) < n:
            result[L-1-n] = 0
        else:
            result[L-1-n] = 1
            num -= 2 ** n
        n -= 1
    return result

def get_mask(line):
    return list(line.split('=')[1].strip())

def powerset(lst):
    L = len(lst)
    return [base10_to_binary(num, L) for num in range(2**L)]

def apply_mask(key, mask):

    X_idxs = []
    bin_num = base10_to_binary(key, 36)
    for i in range(len(bin_num)):
        if mask[i] != '0':
            if mask[i] == '1':
                bin_num[i] = 1
            else:
                bin_num[i] = 'X'
                X_idxs.append(i)

    ps = powerset(X_idxs)
    results = []
    for s in ps:
        bn = bin_num.copy()
        for i in range(len(X_idxs)):
            bn[X_idxs[i]] = s[i]
        results.append(sum([bn[i] * (2 ** (35-i)) for i in range(len(bn))]))

    return results

def store_mem(mem, line, mask):
    line = line.split('=')

    num = int(line[1].strip())
    key = int(line[0].strip().strip('mem[').strip(']'))

    addrs = apply_mask(key, mask)
    for addr in addrs:
        mem[addr] = num


mem = dict()
mask = None
for line in lines:
    if line.startswith("mask"):
        mask = get_mask(line)
    else:
        store_mem(mem, line, mask)

total = sum([mem[k] for k in mem])

print(f"The total is {total}")
