from copy import deepcopy

f = open('input/21a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

allergens_d = dict()
all_ingredients = set()
all_line_ingredients = []

for line in lines:
    idx = line.index('(')
    line_ingredients = [v.strip() for v in line[:idx].strip().split(' ')]
    all_ingredients = all_ingredients.union(set(line_ingredients))
    all_line_ingredients += line_ingredients
    line_allergens = [v.strip() for v in line[idx:].strip().replace('(contains','').replace(')','').strip().split(',')]
    for a in line_allergens:
        if a not in allergens_d:
            allergens_d[a] = [set(line_ingredients)]
        else:
            allergens_d[a].append(set(line_ingredients))

for a in allergens_d:
    allergens_d[a] = set.intersection(*allergens_d[a])

for n in range(len(allergens_d)):
    singletons = [k for k in allergens_d if len(allergens_d[k])==1]
    for k in allergens_d:
        if k not in singletons:
            for s in singletons:
                allergens_d[k] = allergens_d[k] - allergens_d[s]

pairs = [(k, list(allergens_d[k])[0]) for k in allergens_d]
pairs = ",".join([v[1] for v in sorted(pairs, key = lambda x: x[0])])
print(pairs)