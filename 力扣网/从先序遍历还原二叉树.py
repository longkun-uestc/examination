class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def check(s):
    ids1 = 0
    while ids1 < len(s) and s[ids1] == "-":
        ids1 += 1
    count = ids1
    c = 0
    ids2 = -1
    for i in range(ids1, len(s)):
        if s[i] == "-":
            c += 1
        else:
            if c == count:
                ids2 = i
                break
            else:
                c = 0
    if ids2 == -1:
        # print(s[ids1:], "")
        return s[ids1:], ""
    else:
        # print(s[ids1:ids2 - count], s[ids2:])
        return s[ids1:ids2 - count], s[ids2:]


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if len(S) == 0:
            return None
        ids = 0
        while ids < len(S) and S[ids] != "-":
            ids += 1
        val = int(S[:ids])
        node = TreeNode(val)
        left, right = check(S[ids:])
        print(left, ",", right)
        left_node = self.recoverFromPreorder(left)
        right_node = self.recoverFromPreorder(right)
        node.left = left_node
        node.right = right_node
        return node


def pre_order(node, pre_list):
    if node is not None:
        pre_list.append(node.val)
        pre_order(node.left, pre_list)
        pre_order(node.right, pre_list)


def in_order(node, in_list):
    if node is not None:
        in_order(node.left, in_list)
        in_list.append(node.val)
        in_order(node.right, in_list)


if __name__ == '__main__':
    x = "1-401--349---90--88"
    check(x)
    s = Solution()
    result = s.recoverFromPreorder(x)
    a = []
    pre_order(result, a)
    print(a)
    b = []
    in_order(result, b)
    print(b)
