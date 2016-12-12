f = open('input.txt')
regs = dict(a=0,b=0,c=0,d=0)
program = f.readlines()
pc = 0
while True:
    if pc >= len(program):
        break
    parts = program[pc].split()
    inst = parts[0]
    args = parts[1:]
    incval = 1
    if inst == "cpy":
        regs[args[1]] = int(args[0]) if args[0].isdigit() else regs[args[0]]
    elif inst == "jnz":
        if (int(args[0]) if args[0].isdigit() else regs[args[0]]):
            incval = int(args[1])
    elif inst == "inc":
        regs[args[0]] += 1
    elif inst == "dec":
        regs[args[0]] -= 1
    pc += incval


print(regs["a"])
