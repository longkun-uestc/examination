class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        mid = []
        self.mid_order(root, mid)
        print(mid)
        x, y = -1, -1
        for i in range(len(mid)-1):
            if mid[i] > mid[i+1]:
                y = mid[i+1]
                if x == -1:
                    x = mid[i]
                else:
                    break

        def dfs(root):
            if not root:
                return
            if root .val == x or root.val == y:
                root.val = x if root.val == y else y
            dfs(root.left)
            dfs(root.right)
        dfs(root)


    def mid_order(self, root, arr):
        if root:
            self.mid_order(root.left, arr)
            arr.append(root.val)
            self.mid_order(root.right, arr)

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)
    S = Solution()
    S.recoverTree(root)