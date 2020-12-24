from copy import deepcopy

# nums = "389125467" # 23a test input
nums = "916438275"

nums = [int(v) for v in list(nums)]
nums = nums + list(range(max(nums)+1, 1000001))

NUM_MOVES = 10000000
# NUM_MOVES = 100

mm = min(nums)
MM = max(nums)
L = len(nums)

# Always keep current cup at index 0
for n in range(NUM_MOVES):

    if (n+1) % 100 == 0:
        print(f"Move {n+1}")

    current_num = nums[0]
    attempted_destination_num = current_num - 1
    while True:
        if attempted_destination_num in nums[1:4]:
            attempted_destination_num -= 1
        elif attempted_destination_num < mm:
            attempted_destination_num = MM
        else:
            # valid choice
            destination_num = attempted_destination_num
            destination_idx = nums.index(destination_num)
            break

    nums = nums[4:destination_idx] + [destination_num] + nums[1:4] + nums[(destination_idx + 1):] + [current_num]

idx = nums.index(1)
final_nums = [nums[(idx + 1 + i) % L] for i in range(L-1)]

print(f"The resulting cups after 1 are {final_nums[:2]}")
prod = final_nums[0] * final_nums[1]
print(f"The product is {prod}")
