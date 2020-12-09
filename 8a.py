f = open('input/8a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

def parse_instr_line(line):
    (instr, signednum) = line.split(' ')
    instr = instr.strip()
    signednum = signednum.strip()
    sgn = signednum[0]
    num = int(signednum[1:])

    return (instr, sgn, num)

run_instr_idxs = set()
accumulator = 0
idx = 0
while True:

    if idx in run_instr_idxs:
        print(f"Arrived at {idx} a second time!")
        print(f"Accumulator is {accumulator}")
        break

    (instr, sgn, num) = parse_instr_line(lines[idx])

    run_instr_idxs.add(idx)

    if instr == "nop":
        idx += 1
        
    elif instr == "acc":
        if sgn == '+':
            accumulator += num
        else:
            accumulator -= num
        idx += 1

    elif instr == "jmp":
        if sgn == '+':
            idx += num
        else:
            idx -= num

    else:
        print("Uh oh, unknown instruction!")
        print(lines[idx])
        print(instr, sgn, num)
