class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pre_order_left(pRoot, pre_list):
    if pRoot is None:
        pre_list.append(-1)
    else:
        pre_list.append(pRoot.val)
        pre_order_left(pRoot.left, pre_list)
        pre_order_left(pRoot.right, pre_list)

def pre_order_right(pRoot, pre_list):
    if pRoot is None:
        pre_list.append(-1)
    else:
        pre_list.append(pRoot.val)
        pre_order_right(pRoot.right, pre_list)
        pre_order_right(pRoot.left, pre_list)


class Solution:
    def isSymmetrical(self, pRoot):
        if pRoot is None:
            return True
        L1 = []
        L2 = []
        pre_order_left(pRoot, L1)
        pre_order_right(pRoot, L2)
        print(L1, L2)
        return True if L1 == L2 else False




if __name__ == '__main__':
    root = TreeNode(10)
    a = TreeNode(5)
    root.left = a
    left = root.left
    a = TreeNode(4)
    left.left = a
    a = TreeNode(7)
    left.right = a
    a = TreeNode(5)
    root.right = a
    right = root.right
    a = TreeNode(7)
    right.left = a
    a = TreeNode(4)
    right.right = a
    s = Solution()
    a = s.isSymmetrical(root)
    print(a)
