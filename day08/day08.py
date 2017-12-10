from collections import defaultdict
from collections import namedtuple

Instruction = namedtuple('Instruction', ['reg', 'op', 'value',
                                         'cond1', 'condition', 'cond2'])
ops = {'inc': lambda x, y: x + y, 'dec': lambda x, y: x - y}

data = [Instruction(x[0], ops[x[1]], int(x[2]), x[4], x[5], x[6].strip())
        for x in [line.split(' ') for line in open('input.txt').readlines()]]

max_val = 0
regs = defaultdict(int)
for instr in data:
    if eval(str(regs[instr.cond1]) + instr.condition + instr.cond2):
        regs[instr.reg] = instr.op(regs[instr.reg], instr.value)
    if regs[instr.reg] > max_val:
        max_val = regs[instr.reg]
print(max(regs.values()))
print(max_val)
