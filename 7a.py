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

for k0 in d:
    for k1 in d[k0]:
        if k1 in d:
            if 'CAN_BE_INSIDE_OF' not in d[k1]:
                d[k1]['CAN_BE_INSIDE_OF'] = set()
            d[k1]['CAN_BE_INSIDE_OF'].add(k0)

sg_containers = set()

contained = {'shiny gold'}
containers = set()
is_done = False
while not is_done:
    for c in contained:
        if c in d:
            if 'CAN_BE_INSIDE_OF' in d[c]:
                for container in d[c]['CAN_BE_INSIDE_OF']:
                    containers.add(container)
    if len(containers) == 0:
        is_done = True
    else:
        sg_containers = sg_containers.union(containers)
        contained = containers.copy()
        containers = set()

result = sorted(list(sg_containers))
# print(result)
print(len(result))
