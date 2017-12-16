def knot_hash(input_string):
    data = [ord(x) for x in input_string]
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
    return ''.join([format(x, '02x') for x in dense_hash])


class Square:

    def __init__(self, used):
        self.used = used
        self.region = None

    def __str__(self):
        return str(self.used) + ', ' + str(self.region)


grid = [[] for _ in range(128)]
filled = 0
key_string = open('input.txt').read().strip()
for row in range(128):
    row_hash = knot_hash(key_string + '-' + str(row))
    row_bin = bin(int(row_hash, 16))[2:].zfill(128)
    filled += row_bin.count('1')
    grid[row] = [Square(True) if x == '1' else Square(False) for x in row_bin]
print(filled)


def dfs(grid, i, j, region_count):
    grid[i][j].region = region_count
    neighbors = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
    for w in neighbors:
        if 0 <= w[0] < 128 and 0 <= w[1] < 128:
            square = grid[w[0]][w[1]]
            if square.region is None and square.used:
                dfs(grid, w[0], w[1], region_count)


regions = 0
for i in range(128):
    for j in range(128):
        if grid[i][j].region is None and grid[i][j].used:
            dfs(grid, i, j, regions)
            regions += 1
print(regions)
