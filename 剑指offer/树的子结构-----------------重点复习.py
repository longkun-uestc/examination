class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def cmp(t1, t2):
    pre_order(t1)
    print("------", end=" ")
    pre_order(t2)
    print("\n")
    if t2 is None:
        return True
    if t1 is None:
        return False
    if t1.val != t2.val:
        # return cmp(t1.left, t2) or cmp(t1.right, t2)  # 第一类写法
        return False   # 第二类写法
    return cmp(t1.left, t2.left) and cmp(t1.right, t2.right)

# https://www.nowcoder.com/questionTerminal/6e196c44c7004d15b1610b9afca8bd88?answerType=1&f=discussion
# 子结构与子树不同，子结构没有子树那么严格
# 注意是子结构的成立条件
# 第一类写法是有问题的，以为可能出现t1,t2根节点相同，但是仅在t1的子树中存在t2的子树节点，这时候这也会被判断为true
# 例如 t1 = pre_order[8,8,9,2,4,7,7] in_order[9,8,4,2,7,8,7] t2 = pre[8,9,7] in[9,8,7]
# 这时候其实t2不是t1的子结构，但是用第一类写法就会判断为True


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 is None or pRoot2 is None:
            return False
        return cmp(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
        # 注意，首先调用cmp方法，判断跟节点，然后递归调用HasSubTree方法，判断左右节点

def pre_order(node):
    if node is not None:
        print(node.val, end=" ")
        pre_order(node.left)
        pre_order(node.right)


def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.val, end=" ")
        in_order(node.right)

if __name__ == '__main__':
    head = TreeNode(8)
    head.left = TreeNode(8)
    head.right = TreeNode(7)
    a = head.left
    a.left = TreeNode(9)
    a.right = TreeNode(2)
    a = a.right
    a.left = TreeNode(4)
    a.right = TreeNode(7)
    # pre_order(head)
    # print("---------------")
    # in_order(head)
    sub_root = TreeNode(8)
    sub_root.left = TreeNode(9)
    sub_root.right = TreeNode(7)
    s = Solution()
    a = s.HasSubtree(head, sub_root)
    print(a)
