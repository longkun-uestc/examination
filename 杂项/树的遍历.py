class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pre_order(root):
    if not root:
        return
    stack = [root]
    while stack:
        now = stack.pop()
        print(now.val)
        if now.right:
            stack.append(now.right)
        if now.left:
            stack.append(now.left)
def mid_order(root):
    if not root:
        return
    stack = []
    while root:
        stack.append(root)
        root = root.left
    while stack:
        now = stack.pop()
        print(now.val)
        if now.right:
            right = now.right
            while right:
                stack.append(right)
                right = right.left
def mid_order1(root):
    if not root:
        return
    stack = [[root, 0]]
    while stack:
        now, tag = stack[-1]
        if tag == 0:
            stack[-1][1] = 1
            if now.left:
                stack.append([now.left, 0])
        elif tag == 1:
            now, _ = stack.pop()
            print(now.val)
            if now.right:
                stack.append([now.right, 0])


def post_order(root):
    if not root:
        return
    stack = [[root, 0]]
    while stack:
        now, tag = stack[-1]
        if tag == 0:
            stack[-1][1] = 1
            if now.left:
                stack.append([now.left, 0])
        elif tag == 1:
            stack[-1][1] = 2
            if now.right:
                stack.append([now.right, 0])
        else:
            a, tag = stack.pop()
            print(a.val)


def pre_order_recursion(root):
    if root:
        print(root.val)
        pre_order_recursion(root.left)
        pre_order_recursion(root.right)


def mid_order_recursion(root):
    if root:
        mid_order_recursion(root.left)
        print(root.val)
        mid_order_recursion(root.right)


def post_order_recursion(root):
    if root:
        post_order_recursion(root.left)
        post_order_recursion(root.right)
        print(root.val)






if __name__ == '__main__':
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    left = root.left
    left.left = Node(2)
    left.right = Node(4)
    right = root.right
    right.left = Node(6)
    right.right = Node(9)
    right.right.left = Node(8)
    # pre_order(root)
    mid_order1(root)
    # post_order(root)