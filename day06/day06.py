data = [int(x) for x in open('input.txt').read().strip().split("\t")]
seen = []
while data not in seen:
    seen.append(data[:])
    大 = max(data)
    i = data.index(大)
    data[i] = 0
    while 大 > 0:
        i = (i + 1) % len(data)
        data[i] += 1
        大 -= 1
print(len(seen))
print(len(seen) - seen.index(data))
