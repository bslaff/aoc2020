from copy import deepcopy

# nums = "389125467" # 23a test input
nums = "916438275"

nums = [int(v) for v in list(nums)]
nums = nums + list(range(max(nums)+1, 1000001))

NUM_MOVES = 10000000

mm = min(nums)
MM = max(nums)
L = len(nums)

after = [0] * (L + 1) 
for i in range(len(nums) - 1):
    after[nums[i]] = nums[i + 1]
after[nums[L - 1]] = nums[0]

current_num = nums[0]

for n in range(NUM_MOVES):

    attempted_destination_num = current_num - 1
    picked_1 = after[current_num]
    picked_2 = after[picked_1]
    picked_3 = after[picked_2]
    while True:
        if attempted_destination_num == picked_1 or attempted_destination_num == picked_2 or attempted_destination_num == picked_3:
            attempted_destination_num -= 1
        elif attempted_destination_num < mm:
            attempted_destination_num = MM
        else:
            # valid choice
            destination_num = attempted_destination_num
            break

    last_picked_up_num = after[after[after[current_num]]]

    new_after_destination_num = after[current_num]
    new_after_last_picked_up = after[destination_num]
    new_after_current_num = after[after[after[after[current_num]]]]

    after[destination_num] = new_after_destination_num
    after[current_num] = new_after_current_num
    after[last_picked_up_num] = new_after_last_picked_up

    current_num = after[current_num]

a1 = after[1]
a2 = after[a1]

print(f"The resulting cups after 1 are {a1}, {a2}")
print(f"The product is {a1 * a2}")
