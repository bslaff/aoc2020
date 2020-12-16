from math import log2

f = open('input/15a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

nums = [int(v.strip()) for v in lines[0].split(',')]
d = dict()
i = 1
for num in nums:
    last_spoken = num
    last_spoken_in_d = last_spoken in d
    d[num] = [i, 0]
    i += 1
while True:
    if not last_spoken_in_d:
        d[last_spoken] = [i-1, 0]
        now_spoken = 0
    else:
        d[last_spoken] = [i-1, d[last_spoken][0]]
        now_spoken = d[last_spoken][0] - d[last_spoken][1]

    now_spoken_in_d = now_spoken in d

    print(f"{i}: spoke {now_spoken}")
    if i==2020:
        break
    i += 1

    last_spoken = now_spoken
    last_spoken_in_d = now_spoken_in_d

print(f"The result is {now_spoken}")
