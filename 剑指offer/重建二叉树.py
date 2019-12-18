# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre:
            return None
        node = TreeNode(pre[0])
        root_index_in_tin = tin.index(pre[0])
        left_tin = tin[0: root_index_in_tin]
        right_tin = tin[root_index_in_tin + 1:]
        left_pre = pre[1:len(left_tin) + 1]
        right_pre = pre[len(left_tin) + 1:]
        left_node = self.reConstructBinaryTree(left_pre, left_tin)
        right_node = self.reConstructBinaryTree(right_pre, right_tin)
        node.left = left_node
        node.right = right_node
        return node


def pre_order(node):
    if node is not None:
        print(node.val)
        pre_order(node.left)
        pre_order(node.right)


def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.val)
        in_order(node.right)


if __name__ == '__main__':
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    s = Solution()
    node = s.reConstructBinaryTree(pre, tin)
    pre_order(node)
    print("-----------------")
    in_order(node)
