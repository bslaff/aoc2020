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
eye_colors = set([
    "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
])

def is_valid(c):
    a_keys = [z.split(':')[0] for z in c.split(' ')]
    a_vals = [z.split(':')[1] for z in c.split(' ')]
    d = dict()
    for i in range(len(a_keys)):
        d[a_keys[i]] = a_vals[i]

    if len(a_keys) < 7:
        return False

    try:
        if not (len(d["byr"])==4 and int(d["byr"]) >= 1920 and int(d["byr"]) <= 2002):
            return False

        if not (len(d["iyr"])==4 and int(d["iyr"]) >= 2010 and int(d["iyr"]) <= 2020):
            return False

        if not (len(d["eyr"])==4 and int(d["eyr"]) >= 2020 and int(d["eyr"]) <= 2030):
            return False

        if not ( (d["hgt"].endswith("in") or d["hgt"].endswith("cm")) ):
            return False

        units = d["hgt"][-2:]
        height = int(d["hgt"][:-2])
        if (units == "cm" and not (height >= 150 and height <= 193)):
            return False
        if (units == "in" and not (height >= 59 and height <= 76)):
            return False

        if not (len(d["hcl"])==7 and d["hcl"].startswith("#") and sum([x in "1234567890abcdef" for x in d["hcl"][1:]])):
            return False

        if not d["ecl"] in eye_colors:
            return False

        if not (len(d["pid"])==9 and d["pid"].isdigit()):
            return False
        
    except:
        return False # some schema rule was violated

    return True


verdicts = [is_valid(c) for c in candidates]
print(verdicts)
print(sum(verdicts))