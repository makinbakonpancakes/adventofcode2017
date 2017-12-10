data = map(int, open('input.txt').readline().split(','))
rope = list(range(256))
position = 0
skip = 0
for rope_length in data:
    twisted = []
    for x in range(rope_length):
        twisted.append(rope[(position + x) % 256])
    twisted.reverse()
    for x in range(rope_length):
        rope[(position + x) % 256] = twisted[x]
    position += (rope_length + skip) % 256
    skip += 1
print(rope[0] * rope[1])
