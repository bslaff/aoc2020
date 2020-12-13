f = open('input/10a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

nums = [0] + [int(line) for line in lines if len(line) > 0]
nums = sorted(nums)

ones = 0
threes = 0

for i in range(1, len(nums)):
    if nums[i] - nums[i - 1] == 1:
        ones += 1
    elif nums[i] - nums[i - 1] == 3:
        threes += 1

threes += 1 # device adapter

print(f"Ones: {ones}, Threes: {threes}, Ones * Threes: {ones * threes}")