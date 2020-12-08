f = open('input/7a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

def parse_contained_rule(c):
    idx = c.find(' ')
    num_txt = c[:idx].strip()
    if num_txt == 'no':
        num = 0
    else:
        num = int(c[:idx].strip())
    contained_principal = c[(idx + 1):].strip()
    return (contained_principal, num)

def parse_rule(d, line):

    (principal, contains) = line.split('contain')
    principal = principal.strip().replace('bags', '').replace('bag', '').strip()
    contains = contains.split(',')
    contains = [v.strip().strip('.').strip().replace('bags', '').replace('bag', '').strip() for v in contains]
    contains = [parse_contained_rule(c) for c in contains]
    if principal not in d:
        d[principal] = dict()
    for c in contains:
        if c[0] not in d[principal]:
            d[principal][c[0]] = c[1]

    return None
    

d = dict()
for line in lines:
    parse_rule(d, line)

def get_num_contained(d, container_name):

    if d[container_name] == {'other': 0}:
        total = 0
    else:
        total = 0
        for contained in d[container_name]:
            total += d[container_name][contained] * (1 + get_num_contained(d, contained))

    # print(f"Got {total} for {container_name}")
    return total
    
result = get_num_contained(d, 'shiny gold')

print(result)
