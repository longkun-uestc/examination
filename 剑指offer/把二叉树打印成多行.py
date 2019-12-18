# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if pRoot is None:
            return []
        result = []
        q1 = [pRoot]
        q2 = []
        while q1 or q2:
            if q1:
                data = []
                while q1:
                    now = q1.pop(0)
                    if now.left is not None:
                        q2.append(now.left)
                    if now.right is not None:
                        q2.append(now.right)
                    data.append(now.val)
                result.append(data)
            if q2:
                data = []
                while q2:
                    now = q2.pop(0)
                    if now.left is not None:
                        q1.append(now.left)
                    if now.right is not None:
                        q1.append(now.right)
                    data.append(now.val)
                result.append(data)
        print(result)
        return result

if __name__ == '__main__':
    root = TreeNode(8)
    a = TreeNode(6)
    root.left = a
    left = root.left
    a = TreeNode(5)
    left.left = a
    a = TreeNode(7)
    left.right = a
    a = TreeNode(10)
    root.right = a
    right = root.right
    a = TreeNode(9)
    right.left = a
    a = TreeNode(11)
    right.right = a
    s = Solution()
    s.Print(root)
