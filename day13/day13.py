from collections import namedtuple


Scanner = namedtuple('Scanner', ['depth', 'scan_range'])

data = [[x for x in line.strip().split(': ')]
        for line in open('input.txt').readlines()]
firewall = [Scanner(int(x[0]), int(x[1])) for x in data]

severity = 0
for scanner in firewall:
    # The period is (time % (2 * (range - 1)) so if it's zero we get hit
    if scanner.depth % (2 * (scanner.scan_range - 1)) == 0:
        severity += scanner.depth * scanner.scan_range
print(severity)

delay = 10
caught = False
while not caught:
    caught = True
    for scanner in firewall:
        if (scanner.depth + delay) % (2 * (scanner.scan_range - 1)) == 0:
            caught = False
            delay += 1
            break
print(delay)
