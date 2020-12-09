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


def prog_terminates(parsed_lines):

    run_instr_idxs = set()
    accumulator = 0
    idx = 0
    while True:

        if idx == len(parsed_lines):
            # Executing past the last instruction. Terminate!
            print("Program terminated!")
            print(f"Accumulator is {accumulator}")
            return True

        if idx in run_instr_idxs:
            # Arrived a second time! Infinite loop
            return False

        (instr, sgn, num) = parsed_lines[idx]

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

parsed_lines = [parse_instr_line(line) for line in lines]

for change_idx in range(len(parsed_lines)):

    copied_parsed_lines = parsed_lines.copy()

    (instr, sgn, num) = parsed_lines[change_idx]

    if instr == "jmp":
        copied_parsed_lines[change_idx] = ("nop", sgn, num)
    elif instr == "nop":
        copied_parsed_lines[change_idx] = ("jmp", sgn, num)
    else:
        continue

    if prog_terminates(copied_parsed_lines):
        break