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

invalid_num = None

for i in range(PRE_LEN, len(nums)):
    if not is_valid(nums[i], current):
        print(f"Invalid entry {nums[i]} at index {i}.")
        invalid_num = nums[i]
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

i = 0
j = 1
s = nums[i] + nums[j]
if nums[i] < nums[j]:
    MM = nums[j]
    mm = nums[i]
else:
    MM = nums[i]
    mm = nums[j]

while j < len(nums):
    if s == invalid_num:
        print(f"Found contiguous sequence {nums[i:(j+1)]} from index {i} to {j}.")
        print(f"Result is {mm + MM}")
        break
    elif s < invalid_num:
        j += 1
        s += nums[j]
        if nums[j] < mm:
            mm = nums[j]
        if nums[j] > MM:
            MM = nums[j]
    elif s > invalid_num:
        i += 1
        s -= nums[i - 1]
        # could do this with heaps but not necessary yet
        if mm == nums[i - 1]:
            mm = min(nums[i:(j+1)])
        if MM == nums[i - 1]:
            MM = max(nums[i:(j+1)])