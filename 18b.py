from copy import deepcopy

f = open('input/18a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

def evaluate(s):
    s = s.strip().replace(' ', '')
    if len(s) == 1:
        return int(s[0])
    i = 0
    components = []
    while i < len(s):
        if s[i] == '(':
            left_count = 1
            right_count = 0
            j = i + 1
            while left_count > right_count:
                if s[j] == '(':
                    left_count += 1
                elif s[j] == ')':
                    right_count += 1
                j += 1
            expr = s[(i+1):(j-1)]
            components.append(evaluate(expr))
            i = j
        elif s[i] == '+' or s[i] == '*':
            components.append(s[i])
            i += 1
        else:
            components.append(int(s[i]))
            i += 1

    # Now should have no parentheses
    while '+' in components:
        i = components.index('+')
        x = components[i-1] + components[i+1]
        del components[(i-1):(i+2)]
        components.insert(i-1, x)

    # Now should have no parentheses or +
    remaining = [v for v in components if v != '*']
    total = 1
    for v in remaining:
        total *= v

    return total

results = [evaluate(line) for line in lines]
print(f"The results are {results}")
print(f"The sum is {sum(results)}")
