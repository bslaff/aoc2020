import math

f = open('input/12a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

# [east, north]
pos = [0, 0]
waypoint_pos = [10, 1]

def apply_direction(pos, waypoint_pos, line):
    x = line[0]
    num = int(line[1:])
    if x == 'N':
        waypoint_pos[1] += num
    elif x == 'S':
        waypoint_pos[1] -= num
    elif x == 'E':
        waypoint_pos[0] += num
    elif x == 'W':
        waypoint_pos[0] -= num
    elif x == 'L':
        if num == 90:
            waypoint_pos = [-waypoint_pos[1], waypoint_pos[0]]
        elif num == 180:
            waypoint_pos = [-waypoint_pos[0], -waypoint_pos[1]]
        elif num == 270:
            waypoint_pos = [waypoint_pos[1], -waypoint_pos[0]]
        else:
            print("Unexpected degree turn!")
    elif x == 'R':
        if num == 90:
            waypoint_pos = [waypoint_pos[1], -waypoint_pos[0]]
        elif num == 180:
            waypoint_pos = [-waypoint_pos[0], -waypoint_pos[1]]
        elif num == 270:
            waypoint_pos = [-waypoint_pos[1], waypoint_pos[0]]
        else:
            print("Unexpected degree turn!")
    elif x == 'F':
        pos[0] += waypoint_pos[0] * num
        pos[1] += waypoint_pos[1] * num

    return waypoint_pos

print(f"Position {pos}")
print(f"Waypoint {waypoint_pos}")
for line in lines:
    waypoint_pos = apply_direction(pos, waypoint_pos, line)
    print(line)
    print(f"Position {pos}")
    print(f"Waypoint {waypoint_pos}")

print(f"Final distance: {abs(pos[0]) + abs(pos[1])}")