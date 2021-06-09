class Node:
    def __init__(self, idx):
        self.idx = idx
        self.children = []
        self.parent = None
        self.depth = 0

def get_depth(root, colors, color):
    stack = [root]
    count = 0
    while stack:
        now = stack.pop()
        children = now.children
        for c in children:
            if colors[c.idx] == color:
                count += c.depth
            stack.append(c)
    return count

def update_depth(root):
    root.depth = 0
    stack = [root]
    while stack:
        now = stack.pop()
        chidren = now.children
        for c in chidren:
            c.depth = now.depth + 1
            stack.append(c)



if __name__ == '__main__':
    n = int(input())
    color = list(map(int, input().split()))
    color = [-1]+color
    node_list = [Node(i) for i in range(n+1)]
    father = list(map(int, input().split()))
    father = [-1]+father
    for i in range(1, len(father)):
        node_list[i+1].parent = node_list[father[i]]
        node_list[father[i]].children.append(node_list[i+1])
        node_list[i+1].depth = node_list[father[i]].depth + 1
    root = node_list[1]
    for i in range(1, len(node_list)):
        root = node_list[i]
        parent = root.parent
        if parent:
            parent.chidren.remove(root)
            root.children.append(parent)
        update_depth(root)
        col = color[i]
        res = get_depth(root, color, col)







