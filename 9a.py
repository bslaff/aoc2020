from copy import deepcopy

f = open('input/9a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

nums = [int(line) for line in lines if len(line) > 0]

PRE_LEN = 25

current = set()

for i in range(PRE_LEN):
    for j in range(i + 1, PRE_LEN):
        current.add((nums[i] + nums[j], i, j))

def is_valid(num, current):
    for sum_entry in current:
        if num == sum_entry[0]:
            return True
    return False

for i in range(PRE_LEN, len(nums)):
    if not is_valid(nums[i], current):
        print(f"Invalid entry {nums[i]} at index {i}.")
        break
    # Remove influence of outgoing index
    out_i = i - PRE_LEN
    current_copy = deepcopy(current)
    for sum_entry in current_copy:
        if out_i == sum_entry[1] or out_i == sum_entry[2]:
            current.remove(sum_entry)
    # Add influence of incoming index i
    for j in range(i - PRE_LEN, i):
        current.add((nums[i] + nums[j], j, i))

print("Done iterating!")
