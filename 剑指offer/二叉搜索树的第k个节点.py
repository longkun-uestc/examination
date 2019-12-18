class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pre_order(root, pre_list):
    if root is not None:
        pre_list.append(root.val)
        pre_order(root.left, pre_list)
        pre_order(root.right, pre_list)

def search(root, num):
    if root is None:
        return None
    if root.val == num:
        return root
    if root.val < num:
        node1 = search(root.right, num)
        if node1 is not None:
            return node1
    if root.val > num:
        node2 = search(root.left, num)
        if node2 is not None:
            return node2

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if pRoot is None or k < 1:
            return None
        pre_list = []
        pre_order(pRoot, pre_list)
        if len(pre_list) < k:
            return None
        pre_list.sort()
        num = pre_list[k-1]
        node = search(pRoot, num)
        print(num, node.val)
        return node

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
    s.KthNode(root, 0)

