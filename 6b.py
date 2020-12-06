f = open('input/6a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

group_count = 0
total = 0

x = ""
for line in lines:
	if len(line) > 0:
		x += ' ' + line
	else:
		x = x.strip()
		while '  ' in x:
			x = x.replace('  ', ' ')
		x = [set(v) for v in x.split(' ')]
		consensus_replies = set.intersection(*x)
		total += len(set(list(consensus_replies)))
		x = ""

if x != "":
	x = x.strip()
	while '  ' in x:
		x = x.replace('  ', ' ')
	x = [set(v) for v in x.split(' ')]
	consensus_replies = set.intersection(*x)
	total += len(set(list(consensus_replies)))

print(total)
