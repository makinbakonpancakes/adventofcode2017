data = [ord(x) for x in open('input.txt').readline().strip()]
data += [17, 31, 73, 47, 23]
rope = list(range(256))
position = 0
skip = 0
for _ in range(64):
    for rope_length in data:
        twisted = []
        for x in range(rope_length):
            twisted.append(rope[(position + x) % 256])
        twisted.reverse()
        for x in range(rope_length):
            rope[(position + x) % 256] = twisted[x]
        position += (rope_length + skip) % 256
        skip += 1

dense_hash = []
for x in range(0, 256, 16):
    dense_num = rope[x]
    for y in range(15):
        dense_num = dense_num ^ rope[x + y + 1]
    dense_hash.append(dense_num)
print(''.join([format(x, '02x') for x in dense_hash]))
