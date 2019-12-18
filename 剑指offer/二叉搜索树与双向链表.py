class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def to_list(pRootOfTree):
    if pRootOfTree is None:
        return None
    if pRootOfTree.left is None and pRootOfTree.right is None:
        return pRootOfTree

    left_list = to_list(pRootOfTree.left)
    if left_list is not None:
        while left_list.right is not None:
            left_list = left_list.right
        pRootOfTree.left = left_list
        left_list.right = pRootOfTree
    right_list = to_list(pRootOfTree.right)
    if right_list is not None:
        while right_list.left is not None:
            right_list = right_list.left
        pRootOfTree.right = right_list
        right_list.left = pRootOfTree
    # l = pRootOfTree
    # while l.left is not None:
    #     l = l.left
    # while l is not None:
    #     print(l.val, end=" ")
    #     l = l.right
    # print("\n")
    return pRootOfTree

class Solution:
    def Convert(self, pRootOfTree):
        if pRootOfTree is None:
            return None
        res = to_list(pRootOfTree)
        while res.left is not None:
            res = res.left
        return res


if __name__ == '__main__':
    head = TreeNode(10)
    a = TreeNode(6)
    head.left = a
    left = head.left
    a = TreeNode(4)
    left.left = a
    a = TreeNode(8)
    left.right = a
    a = TreeNode(14)
    head.right = a
    right = head.right
    a = TreeNode(12)
    right.left = a
    a = TreeNode(16)
    right.right = a
    s = Solution()
    result = s.Convert(head)
    l = result
    while l.left is not None:
        l = l.left
    print("left:", end=" ")
    while l is not None:
        print(l.val, end=" ")
        l = l.right
    print("\n")
    r = result
    while r.right is not None:
        r = r.right
    print("right:", end=" ")
    while r is not None:
        print(r.val, end=" ")
        r = r.left

