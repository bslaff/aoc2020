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
		while ' ' in x:
			x = x.replace(' ', '')
		group_replies = x.strip()
		total += len(set(list(group_replies)))
		x = ""

if x != "":
	while ' ' in x:
		x = x.replace(' ', '')
	group_replies = x.strip()
	total += len(set(list(group_replies)))

print(total)
