from copy import deepcopy

# nums = "389125467" # 23a test input
nums = "916438275"

nums = [int(v) for v in list(nums)]

NUM_MOVES = 100

mm = min(nums)
MM = max(nums)
L = len(nums)

# Always keep current cup at index 0
for n in range(NUM_MOVES):

    current_num = nums[0]
    picked_up_nums = [nums[i] for i in range(1, 4)]
    attempted_destination_num = current_num - 1
    while True:
        if attempted_destination_num in picked_up_nums:
            attempted_destination_num -= 1
        elif attempted_destination_num < mm:
            attempted_destination_num = MM
        else:
            # valid choice
            destination_num = attempted_destination_num
            destination_idx = nums.index(destination_num)
            break

    new_nums = [0] * L
    new_nums[L-1] = current_num
    r = 0
    offset = 3
    while r < L-1:
        if r + 1 + offset == destination_idx:
            new_nums[r] = nums[r + 1 + offset]
            for j in range(1, 4):
                new_nums[r + j] = nums[j]
            offset = 0
            r += 4
        else:
            new_nums[r] = nums[r + 1 + offset]
            r += 1

    nums = new_nums

idx = nums.index(1)
final_nums = [nums[(idx + 1 + i) % L] for i in range(L-1)]

print(f"The result is {''.join([str(v) for v in final_nums])}")
