class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def depth(pRoot):
    if pRoot is None:
        return 0
    if pRoot.left is None and pRoot.right is None:
        return 1
    else:
        return max(depth(pRoot.left), depth(pRoot.right)) + 1

class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot is None:
            return True
        if pRoot.left is None and pRoot.right is None:
            return True
        # 这种方法是先整体判断，再判断局部，如果整体都不是，那后面的也不用找了
        left = depth(pRoot.left)
        right = depth(pRoot.right)
        flag = True if abs(left-right) <= 1 else False
        return flag and self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
        # 两种方法都可以,各有千秋。下面这种是先找最小非平衡二叉树，找到了之后后面的都不用再找了
        # left_check = self.IsBalanced_Solution(pRoot.left)
        # right_check = self.IsBalanced_Solution(pRoot.right)
        # left = depth(pRoot.left)
        # right = depth(pRoot.right)
        # flag = True if abs(left - right) <= 1 else False
        # return left_check and right_check and flag


def check(pRoot):
    if pRoot is None:
        return True
    if pRoot.left is None and pRoot.right is None:
        return True
    # left = depth(pRoot.left)
    # right = depth(pRoot.right)
    # flag = True if abs(left-right) <= 1 else False
    # return flag and check(pRoot.left) and check(pRoot.right)
    left_check = check(pRoot.left)
    right_check = check(pRoot.right)
    left = depth(pRoot.left)
    right = depth(pRoot.right)
    flag = True if abs(left-right) <= 1 else False
    return left_check and right_check and flag
