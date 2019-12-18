class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if root is None:
            return []
        stack = [root]
        result = []
        while stack:
            now = stack.pop(0)
            result.append(now.val)
            if now.left:
                stack.append(now.left)
            if now.right:
                stack.append(now.right)
        return result
