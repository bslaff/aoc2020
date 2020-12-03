f = open('1a_input.txt', 'r')
lines = f.readlines()
f.close()

nums = sorted([int(v.strip()) for v in lines if len(v.strip())>0])
i = 0
j = len(nums) - 1
while True:
    a = nums[i]
    b = nums[j]

    while a + b > 2020:
        j -= 1
        b = nums[j]

    if a + b == 2020:
        print("Got it")
        print(a)
        print(b)
        print(a+b)
        print(a*b)
        exit()

    i += 1
