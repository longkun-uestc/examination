class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_father(root, node1, node2):
    if not root:
        return 0
    node = search(root, node1, node2)
    layer, flag = get_layer(root, node)
    queue = [root]
    length = len(queue)
    tmp = []
    cnt = 0
    while queue:
        tmp = []
        for _ in range(length):
            now = queue.pop(0)
            if now.left:
                queue.append(now.left)
            if now.right:
                queue.append(now.right)
            tmp.append(now.val)
        if cnt == layer:
            break
        cnt += 1
        length = len(queue)
    return sum(tmp)



def get_layer(root, node):
    if not root:
        return 0, 0
    if root == node:
        return 0, 1
    else:
        x1, y1 = get_layer(root.left, node)
        x2, y2 = get_layer(root.right, node)
        a = (x1+1)*y1
        b = (x2+1)*y2
        return max(a, b), 0 if y1 == 0 and y2 == 0 else 1

def search(root, node1, node2):
    if not root:
        return None
    a, b = pre_order(root.left, node1, node2)
    if a and not b or not a and b:
        return root
    elif a and b:
        return search(root.left, node1, node2)
    else:
        return search(root.right, node1, node2)

def pre_order(root, node1, node2):
    if not root:
        return False, False
    x1, x2 = False, False
    if root == node1:
        x1 = True
    if root == node2:
        x2 = True
    a1, b1 = pre_order(root.left, node1, node2)
    a2, b2 = pre_order(root.right, node1, node2)
    return x1 or a1 or a2, x2 or b1 or b2


if __name__ == '__main__':
    root = Node(5)
    root.left = Node(3)
    root.right=Node(7)
    left = root.left
    left.left = Node(2)
    left.right = Node(4)
    node1 = left.left
    node2 = root.right
    # res = search(root, node1, node2)
    # print(res.val)
    x = get_father(root, node1, node2)
    print(x)


