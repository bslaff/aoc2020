from copy import deepcopy

f = open('input/19a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

rules_d = dict()
images = []

for line in lines:
    if ':' in line:
        line = line.split(':')
        key = int(line[0])
        rules = [[x.replace('"','') for x in v.split(' ') if len(x)>0] for v in line[1].split('|')]
        rules_d[key] = rules
    else:
        if len(line) > 0:
            images.append(line.strip())

for key in rules_d:
    for i in range(len(rules_d[key])):
        if all([x.isalpha() for x in rules_d[key][i]]):
            rules_d[key][i] = "".join(rules_d[key][i])
        else:
            for j in range(len(rules_d[key][i])):
                try:
                    x = int(rules_d[key][i][j])
                    rules_d[key][i][j] = x
                except ValueError:
                    pass
                except TypeError:
                    pass
    if len(rules_d[key]) == 1 and isinstance(rules_d[key][0], str):
        rules_d[key] = [rules_d[key][0]]

print(f"The rules are {rules_d}")
print(f"The images are {images}")

while True:
    made_change = False
    for key in rules_d:
        if isinstance(rules_d[key][0], str):
            # fully resolved list of strings
            continue
        if all([all([isinstance(rules_d[k][0], str) for k in rules_d[key][i]]) for i in range(len(rules_d[key]))]):
            final_results = []
            for i in range(len(rules_d[key])):
                results = ['']
                for k in rules_d[key][i]:
                    resolved_strs = rules_d[k]
                    new_results = []
                    for v in results:
                        for r in resolved_strs:
                            new_results.append(v + r)
                    results = deepcopy(new_results)
                rules_d[key][i] = deepcopy(results)
                final_results += deepcopy(results)
            rules_d[key] = final_results
            made_change = True
    if not made_change:
        break

results = [image in rules_d[0] for image in images]
print(f"The number of matches is {sum(results)}")