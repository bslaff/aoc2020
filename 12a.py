import math

f = open('input/12a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

# [east, north]
pos = [0, 0]
# degrees, east==0 as in the trig convention
facing = 0

def apply_direction(pos, facing, line):
    x = line[0]
    num = int(line[1:])
    if x == 'N':
        pos[1] += num
    elif x == 'S':
        pos[1] -= num
    elif x == 'E':
        pos[0] += num
    elif x == 'W':
        pos[0] -= num
    elif x == 'L':
        facing = (facing + num) % 360
    elif x == 'R':
        facing = (facing - num) % 360
    elif x == 'F':
        unit = None
        if facing == 90:
            unit = [0, 1]
        elif facing == 270:
            unit = [0, -1]
        else:
            t = math.sqrt(math.tan(math.radians(facing)) ** 2)
            mag = math.sqrt(1 + t**2)
            if facing >= 270 and facing < 360:
                unit = [1/mag, -t/mag]
            elif facing >= 180 and facing < 270:
                unit = [-1/mag, -t/mag]
            elif facing >= 90 and facing < 180:
                unit = [-1/mag, t/mag]
            else:
                unit = [1/mag, t/mag]
        pos[0] += unit[0] * num
        pos[1] += unit[1] * num

    return facing


for line in lines:
    facing = apply_direction(pos, facing, line)

print(f"Final distance: {abs(pos[0]) + abs(pos[1])}")