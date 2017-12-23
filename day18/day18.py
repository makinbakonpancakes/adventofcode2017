from collections import defaultdict
from threading import Thread
from queue import Queue
import logging


def part1(cmds):
    reg = defaultdict(int)

    def val(reg_or_num):
        try:
            return int(reg_or_num)
        except ValueError:
            return reg[reg_or_num]

    played = None
    received = []
    i = 0
    while i < len(cmds):
        cmd, args = cmds[i]
        x, *y = args
        y = y[0] if y else y
        if cmd == 'snd':
            played = reg[x]
        elif cmd == 'set':
            reg[x] = val(y)
        elif cmd == 'add':
            reg[x] += val(y)
        elif cmd == 'mul':
            reg[x] *= val(y)
        elif cmd == 'mod':
            reg[x] = reg[x] % val(y)
        elif cmd == 'rcv':
            if val(x) != 0:
                received.append(played)
                break
        elif cmd == 'jgz':
            if val(x) > 0:
                i += val(y)
                continue
        i += 1
    return received[0]


def run_program(num, cmds, my_q, other_q, one_count=0):
    reg = defaultdict(int)
    reg['p'] = num

    def val(reg_or_num):
        try:
            return int(reg_or_num)
        except ValueError:
            return reg[reg_or_num]

    received = []
    i = 0
    while i < len(cmds) and i >= 0:
        cmd, args = cmds[i]
        x, *y = args
        y = y[0] if y else None
        if cmd == 'snd':
            if x == 1:
                one_count += 1
            other_q.put(val(x))
        elif cmd == 'set':
            reg[x] = val(y)
        elif cmd == 'add':
            reg[x] += val(y)
        elif cmd == 'mul':
            reg[x] *= val(y)
        elif cmd == 'mod':
            reg[x] = reg[x] % val(y)
        elif cmd == 'rcv':
            if val(x) != 0:
                # Is it cheating to use a timeout?
                rcv_val = my_q.get(True, 5)
                my_q.task_done()
                received.append(rcv_val)
        elif cmd == 'jgz':
            if val(x) > 0:
                i += val(y)
                continue
        i += 1


def part2(cmds):
    q1 = Queue()
    q2 = Queue()
    ones_sent = 0
    prog_1 = Thread(target=run_program, args=(0, cmds, q1, q2, ones_sent))
    prog_1.daemon = True
    prog_2 = Thread(target=run_program, args=(1, cmds, q2, q1))
    prog_2.daemon = True

    prog_1.start()
    prog_2.start()

    q1.join()
    q2.join()

    return ones_sent


data = [line.strip().split(' ') for line in open('input.txt').readlines()]
cmds = [[x[0], x[1:]] for x in data]

print(part1(cmds))
# Not done yet
# print(part2(cmds))
