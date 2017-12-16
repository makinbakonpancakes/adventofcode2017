dance = open('input.txt').read().split(',')
programs = [chr(x) for x in range(97, 113)]


def party():
    global programs
    for move in dance:
        if move[0] == 's':
            n = int(move[1:])
            programs = programs[-n:] + programs[:-n]
        elif move[0] == 'x':
            swap = [int(x) for x in move[1:].split('/')]
            programs[swap[0]], programs[swap[1]] = programs[swap[1]], \
                                                   programs[swap[0]]
        elif move[0] == 'p':
            partner = move[1:].split('/')
            a, b = programs.index(partner[0]), programs.index(partner[1])
            programs[a], programs[b] = programs[b], programs[a]


seen = [''.join(programs)]
party()
print(''.join(programs))
seen.append(''.join(programs))
for x in range(1, 10**9):
    party()
    if ''.join(programs) in seen:
        break
    seen.append(''.join(programs))
for _ in range(10**9 % len(seen)):
    party()
print(''.join(programs))
