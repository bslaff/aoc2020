f = open('input/4a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()
candidates = []
x = ""
for line in lines:
    if len(line) > 0:
        x += ' ' + line
    else:
        candidates.append(x.replace('  ', ' ').replace('  ', ' ').strip())
        x = ""

if x != "":
    candidates.append(x.replace('  ', ' ').replace('  ', ' ').strip())

pw_keys = set([
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid"
])

def is_valid(c):
    a = [z.split(':')[0] for z in c.split(' ')]
    if len(a) < 7:
        return False

    num_keys = sum([k in pw_keys for k in a])
    if num_keys == len(pw_keys):
        return True

    return not ("cid" in a)

verdicts = [is_valid(c) for c in candidates]
print(verdicts)
print(sum(verdicts))