class Node(object):
    def __init__(self, index):
        self.index = index
        self.children = []
        self.children_num = 0
        self.father = 0
def get_father(root, nodes, u, v):
    if root.index == u or root.index == v:
        return root.index
    children = root.children
    x = -1
    y = -1
    for ch in children:
        if x == -1:
            x = get_father(nodes[ch-1], nodes, u, v)
        else:
            y = get_father(nodes[ch-1], nodes, u, v)
    if x != -1 and y != -1:
        return root.index
    elif x != -1 and y == -1:
        return x
    elif x == -1 and y != -1:
        return y
    else:
        return -1

def is_father(nodes, u, v):
    now = nodes[v-1]
    father = now.father
    while father != u and father != 0:
        node = nodes[father-1]
        father = node.father
    if father == u:
        return True
    else:
        return False


if __name__ == '__main__':
    n = int(input())
    nodes = [Node(i+1) for i in range(n)]
    for i in range(n-1):
        u, v = list(map(int, input().split()))
        nodes[u-1].children.append(v)
        nodes[v-1].children.append(u)
    nums = list(map(int, input().split()))
    root = None
    for i, num in enumerate(nums):
        nodes[i].children_num = num
        if num == len(nodes[i].children):
            root = nodes[i]
        # if num == 0:
        #     keys = list(nodes[i].flag.keys())
        #     key = keys[0]
        #     nodes[i].flag[key-1] = False
        #     nodes[i].children.remove(key)
        #     nodes[i].father = key
        # if num == len(nodes[i].children):
        #     root = nodes[i]
        #     children = root.children
        #     for ch in children:
        #         nodes[ch-1].flag[i+1] = False
        #         nodes[ch-1].father = i+1
                # nodes[ch-1].children.remove(i+1)
    queue = [root.index]
    while queue:
        now_index = queue.pop(0)
        now = nodes[now_index-1]
        children = now.children
        for ch in children:
            nodes[ch-1].children.remove(now.index)
            nodes[ch-1].father = now.index
            queue.append(ch)
    q = int(input())
    for _ in range(q):
        u, v = list(map(int, input().split()))
        if is_father(nodes, u, v):
            print("ZZZZ")
        elif is_father(nodes, v, u):
            print("SSSS")
        else:
            index = get_father(root, nodes, u, v)
            print(index)







