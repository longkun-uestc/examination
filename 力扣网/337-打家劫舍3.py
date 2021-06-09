class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
dp = {}
class Solution:
    def rob(self, root: TreeNode) -> int:
        # res = self.rob1(root, True)
        # print(res)
        # return res
        v1, v2 = self.rob2(root)
        return max(v1, v2)

    def rob1(self, root):
        if not root:
            return 0
        if root in dp:
            return dp[root]
        else:
            money = root.val
            if root.left:
                money += self.rob1(root.left.left) + self.rob1(root.left.right)
            if root.right:
                money += self.rob1(root.right.left) + self.rob1(root.right.right)
            money1 = self.rob1(root.left) + self.rob1(root.right)
            dp[root] = max(money, money1)
            return dp[root]


    def rob2(self, root):
        if not root:
            return 0, 0
        left = self.rob2(root.left)
        right = self.rob2(root.right)
        v1 = root.val + left[1] + right[1]
        v2 = max(left) + max(right)
        return v1, v2

if __name__ == '__main__':
    # root = TreeNode(3)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # left = root.left
    # right = root.right
    # left.right = TreeNode(3)
    # right.right = TreeNode(1)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    s = Solution()
    s.rob(root)

    # 3
    # {(11438016, True): 0, (11438016, False): 0, (140607610153376, True): 3, (140607610824304, False): 3,
    #  (140607610153040, True): 1, (140607619642896, False): 1, (140607610153376, False): 0, (140607610824304, True): 3,
    #  (140607610153040, False): 0, (140607619642896, True): 3, (140607588195584, True): 1, (140607588296592, True): 3,
    #  (140607610152224, False): 4, (140607588296688, True): 1, (140607588194912, False): 1, (140607588195584, False): 0,
    #  (140607588296592, False): 0, (140607610152224, True): 4, (140607588296688, False): 0, (140607588194912, True): 5,
    #  (140607610824832, False): 0, (140607610824832, True): 2}
    # 11438016
    # 140607619644816
    # 140607610824832
    # 140607610153040