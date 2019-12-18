class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 路径的定义
# 输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)

# 这种写法不符合路径的定义, 他可以查找树中，从根节点到其他任意节点的和等于number的路线
def find(root, number):
    if root is None or root.val > number:
        return []
    if root.val == number:
        return [[number]]
    else:
        result = []
        left = find(root.left, number - root.val)
        if left:
            for l in left:
                l.insert(0, root.val)
                result.append(l)
        right = find(root.right, number - root.val)
        if right:
            for r in right:
                r.insert(0, root.val)
                result.append(r)
        return result


def new_find(root, number):
    if root.left is None and root.right is None:
        if number == root.val:
            return [[number]]
        else:
            return []
    else:
        result = []
        if root.left is not None:
            left = new_find(root.left, number - root.val)
            for l in left:
                l.insert(0, root.val)
                result.append(l)
        if root.right is not None:
            right = new_find(root.right, number - root.val)
            for r in right:
                r.insert(0, root.val)
                result.append(r)
        return result

    # if root.val == number:
    #     return [[number]]
    # else:
    #     result = []
    #     left = find(root.left, number-root.val)
    #     if left:
    #         for l in left:
    #             l.insert(0, root.val)
    #             result.append(l)
    #     right = find(root.right, number-root.val)
    #     if right:
    #         for r in right:
    #             r.insert(0, root.val)
    #             result.append(r)
    #     return result


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if root is None or root.val > expectNumber:
            return []
        all = new_find(root, expectNumber)
        all.sort(key=lambda obj: len(obj), reverse=True)
        return all


if __name__ == '__main__':
    root = TreeNode(10)
    a = TreeNode(5)
    root.left = a
    left = root.left
    a = TreeNode(4)
    left.left = a
    a = TreeNode(7)
    left.right = a
    a = TreeNode(12)
    root.right = a
    s = Solution()
    a = s.FindPath(root, 12)
    print(a)
