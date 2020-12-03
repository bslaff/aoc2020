def get_pw(line):
    ddd = dict()
    a = line.split(':')
    ddd['pw'] = a[1].strip()
    b = a[0].strip()
    c = b.split(' ')
    ddd['letter'] = c[1].strip()
    d = c[0].strip()
    e = d.split('-')
    upper = int(e[1].strip())
    lower = int(e[0].strip())
    ddd['upper'] = upper
    ddd['lower'] = lower
    return ddd

def is_valid(d):
    is_lower = d['pw'][d['lower']-1] == d['letter']
    is_higher = d['pw'][d['upper']-1] == d['letter']
    return sum([is_lower, is_higher]) == 1


f = open('2a_input.txt', 'r')
lines = f.readlines()
f.close()

passwords = [get_pw(line.strip()) for line in lines if len(line)>0]
valid = [is_valid(pw) for pw in passwords]

print(f"{sum(valid)} of {len(passwords)} were valid")
