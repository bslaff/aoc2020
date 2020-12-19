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
    num_resolved = 0
    resolved_record = []
    for key in rules_d:
        if isinstance(rules_d[key][0], str):
            # fully resolved list of strings
            num_resolved += 1
            resolved_record.append(key)
            continue
        if key in [8, 11]:
            continue # don't even try to resolve these yet
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
    print(f"{num_resolved} of {len(rules_d)} are resolved")
    unresolved = [k for k in rules_d if k not in resolved_record]
    print(f"Unresolved: {unresolved}") 
    if not made_change:
        break

# Only 8, 11, and 0 ultimately are unresolved! good... 
# 0: 8 11
# 8: 42 | 42 8              # we can repeat rule 42 as many times as we want
# 11: 42 31 | 42 11 31      # likewise we can repeat 42 as many times as we want followed by 31 the same number of times

# so valid matches do the following: end with 31 matching K times, prior to that match 42 at least K + 1 times, and have nothing else.
matching = []
for i in range(len(images)):
    image = deepcopy(images[i])
    num_42 = 0
    found = False
    while True:
        for match in rules_d[42]:
            if match == image[:len(match)]:
                found = True
                image = image[len(match):]
                num_42 += 1
        if not found:
            break
        found = False
    num_31 = 0
    found = False
    while True:
        for match in rules_d[31]:
            if match == image[:len(match)]:
                found = True
                image = image[len(match):]
                num_31 += 1
        if not found:
            break
        found = False
    
    # valid matches do the following: end with 31 matching K times, prior to that match 42 at least K + 1 times, and have nothing else.
    if num_42 >=2 and num_31 >= 1 and num_42 > num_31 and len(image) == 0:
        matching.append(images[i])

print(f"The number of matches is {len(matching)} out of the original {len(images)}")