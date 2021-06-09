class Node:
    def __init__(self, idx):
        self.id = idx
        self.children = []
        self.path = 0
        self.parent = None

n = int(input())
nodes = [Node(i) for i in range(n+1)]
for i in range(n-1):
    s, e, w = list(map(int, input().split()))
    nodes[s].children.append((e, w))
    nodes[e].parent = s
queue = [nodes[1]]
path1 = 0
max_path = -1
total_weight = 0
while queue:
    node = queue.pop(0)
    for idx, w in node.children:
        nodes[idx].path = node.path + w
        total_weight += w
        max_path = max(max_path, nodes[idx].path)
        queue.append(nodes[idx])
        path1 += nodes[idx].path
print(path1, total_weight*2-max_path)



