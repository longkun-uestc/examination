class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        if pRoot is None:
            return []
        q1 = []
        q2 = []
        result = []
        q1.append(pRoot)
        flag = "L"
        while q1 or q2:
            a = [x.val for x in q1]
            b = [x.val for x in q2]
            print(a, b)
            if flag == "L":
                l = []
                while q1:
                    node = q1.pop()
                    if node.left is not None:
                        q2.append(node.left)
                    if node.right is not None:
                        q2.append(node.right)
                    l.append(node.val)
                result.append(l)
                flag = "R"
            elif flag == "R":
                r = []
                while q2:
                    node = q2.pop()
                    if node.right is not None:
                        q1.append(node.right)
                    if node.left is not None:
                        q1.append(node.left)
                    r.append(node.val)
                result.append(r)
                flag = "L"
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


