data = [x.strip().split(' ') for x in open('input.txt').readlines()]
tower = {}
not_roots = set()
for tree in data:
    name = tree[0]
    weight = int(tree[1][1:-1])
    forest = [x.strip(',') for x in tree[3:]]
    not_roots.update(forest)
    tower[name] = (weight, forest)
root = (tower.keys() - not_roots).pop()
print(root)
