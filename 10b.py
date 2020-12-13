f = open('input/10a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

nums = sorted([0] + [int(line) for line in lines if len(line) > 0])
nums = nums + [nums[-1] + 3]

def count(idx, nums, d):

    if nums[idx] in d:
        return d[nums[idx]]

    if idx == 0:
        result = 1
    else:
        c_idx = idx - 1
        result = 0
        while nums[idx] - nums[c_idx] <= 3 and c_idx >= 0:
            result += count(c_idx, nums, d)
            c_idx -= 1

    if nums[idx] not in d:
        d[nums[idx]] = result

    return result

d = dict()
for i in range(len(nums)):
    count(i, nums, d)

print(f"Result: {d[nums[-1]]}")