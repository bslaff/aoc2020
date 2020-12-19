from copy import deepcopy

f = open('input/18a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

def evaluate(s):
    s = s.strip().replace(' ', '')
    if len(s) == 1:
        return int(s[0])
    i = 0
    total = 0
    current_op = '+'
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
            if current_op == '+':
                total += evaluate(expr)
            elif current_op == '*':
                total *= evaluate(expr)
            i = j
        elif s[i] == '+':
            current_op = '+'
            i += 1
        elif s[i] == '*':
            current_op = '*'
            i += 1
        else:
            # integer case
            if current_op == '+':
                total += int(s[i])
            elif current_op == '*':
                total *= int(s[i])
            i += 1

    return total

results = [evaluate(line) for line in lines]
print(f"The results are {results}")
print(f"The sum is {sum(results)}")
