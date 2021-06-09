from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def postor_order(root, array):
    if root is None:
        return
    postor_order(root.left, array)
    postor_order(root.right, array)
    array.append(root.val)

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        递归方式
        :param root:
        :return:
        '''
        result = []
        postor_order(root, result)
        return result

    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        '''
        非递归方式
        :param root:
        :return:
        '''
        if root is None:
            return []
        result = []
        stack = [[root, "L"]]
        while stack:
            now, flag = stack[-1]
            if flag == "L":
                stack[-1][1] = "R"
                if now.left is not None:
                    stack.append([now.left, "L"])
            elif flag == "R":
                stack[-1][1] = "S"
                if now.right is not None:
                    stack.append([now.right, "L"])
            elif flag == "S":
                result.append(now.val)
                stack.pop()
        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    left = root.left
    left.left = TreeNode(2)
    left.right = TreeNode(6)
    left.right.left = TreeNode(5)
    s = Solution()
    s.postorderTraversal1(root)