from collections import namedtuple
import sys


Node = namedtuple('Node', ['weight', 'children'])
data = [x.strip().split(' ') for x in open('input.txt').readlines()]
tower = {}
not_roots = set()
for tree in data:
    name = tree[0]
    weight = int(tree[1][1:-1])
    forest = [x.strip(',') for x in tree[3:]]
    not_roots.update(forest)
    tower[name] = Node(weight, forest)
root = (tower.keys() - not_roots).pop()
print(root)


def tower_weight(name):
    if len(tower[name].children) == 0:
        return tower[name].weight
    else:
        weights = {x: tower_weight(x) for x in tower[name].children}
        if len(set(weights.values())) != 1:
            bad_node = [x for x in weights.items()
                        if list(weights.values()).count(x[1]) == 1][0]
            good_node = [x for x in weights.items()
                         if list(weights.values()).count(x[1]) != 1][0]
            print(tower[bad_node[0]].weight - abs(good_node[1] - bad_node[1]))
            sys.exit(0)
        return sum([x[1] for x in weights.items()]) + tower[name].weight


tower_weight(root)
