
def find_result(nums, target):

    i = 0
    j = len(nums) - 1

    while True:
        a = nums[i]
        b = nums[j]

        while a + b > target:
            j -= 1
            if i==j:
                return (False, None, None)
            b = nums[j]

        if a + b == target:
            return (True, a, b)

        i += 1
        if i==j:
            return (False, None, None)

f = open('1a_input.txt', 'r')
lines = f.readlines()
f.close()

nums = sorted([int(v.strip()) for v in lines if len(v.strip())>0])

for idx in range(len(nums)):

    nums_x = [nums[k] for k in range(len(nums)) if k != idx]

    target = 2020 - nums[idx]

    (got_result, aaa, bbb) = find_result(nums_x, target)

    if got_result:
        sorted_result = sorted([nums[idx], aaa, bbb])
        (aa, bb, cc) = (sorted_result[0], sorted_result[1], sorted_result[2])
        print("Got result")
        print(aa)
        print(bb)
        print(cc)
        print(aa + bb + cc)
        print(aa * bb * cc)
        print("Done")