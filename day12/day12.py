class Node:

    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors
        self.discovered = False


pipes = [line.strip().split(' <-> ') for line in open('input.txt')]
graph = [Node(int(x[0]), [int(y) for y in x[1].split(', ')]) for x in pipes]


def dfs(v):
    graph[v.name].discovered = True
    for w in graph[v.name].neighbors:
        if not graph[w].discovered:
            dfs(graph[w])


dfs(graph[0])
print(len([x for x in graph if x.discovered]))
groups = 1
for node in graph:
    if not node.discovered:
        groups += 1
        dfs(node)
print(groups)
