class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def check(q):
    for node in q:
        if node.val != "#":
            return True
    return False

def cut(root):
    if root is None:
        return
    print(root.val)
    if root.left is not None and root.left.val == "#":
        root.left = None
    if root.right is not None and root.right.val == "#":
        root.right = None
    cut(root.left)
    cut(root.right)

class Solution:
    def Serialize(self, root):
        if root is None:
            return []
        q1 = [root]
        q2 = []
        result = []
        while q1 or q2:
            # a = [x.val for x in q1]
            # b = [x.val for x in q2]
            # print(a, b)
            q1 = q1 if check(q1) else []
            # a = [x.val for x in q1]
            # b = [x.val for x in q2]
            # print(a, b, result)
            while q1:
                node = q1.pop(0)
                q2.append(node.left if node.left is not None else TreeNode("#"))
                q2.append(node.right if node.right is not None else TreeNode("#"))
                result.append(node.val)
            q2 = q2 if check(q2) else []
            while q2:
                node = q2.pop(0)
                q1.append(node.left if node.left is not None else TreeNode("#"))
                q1.append(node.right if node.right is not None else TreeNode("#"))
                result.append(node.val)
        while result[-1] == "#":
            result.pop()
        # s = ""
        # for r in result:
        #     s += str(r)
        # s += "!"
        # print(s)
        print(result)
        return result
        # write code here

    def Deserialize(self, s):
        if len(s) == 0:
            return None
        head = TreeNode(s[0])
        queue = [head]
        i = 1
        flag = 'L'
        for i in range(1, len(s)):
            if flag == "L":
                now = queue.pop(0)
            node = TreeNode(s[i])
            if flag == "L":
                now.left = node
                flag = "R"
            else:
                now.right = node
                flag = "L"
            queue.append(node)
        cut(head)
        return head

def pre_order(root, pre_list):
    if root is not None:
        pre_list.append(root.val)
        pre_order(root.left, pre_list)
        pre_order(root.right, pre_list)



if __name__ == '__main__':
    root = TreeNode(8)
    a = TreeNode(6)
    root.left = a
    left = root.left
    a = TreeNode(5)
    left.left = a
    # a = TreeNode(7)
    # left.right = a
    a = TreeNode(10)
    root.right = a
    right = root.right
    a = TreeNode(9)
    right.left = a
    a = TreeNode(11)
    right.right = a
    right = right.right
    a = TreeNode(13)
    right.left = a
    s = Solution()
    serial = s.Serialize(root)
    pre_list = []
    node = s.Deserialize(serial)
    pre_order(node, pre_list)
    print(pre_list)
    cut(node)
    a = []
    pre_order(node, a)
    print(a)
