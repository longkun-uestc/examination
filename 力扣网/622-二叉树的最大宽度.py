class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree1(self, root: TreeNode) -> int:
        if not root:
            return 0
        q1 = [root]
        q2 = []
        max_l = 0
        while q1 or q2:
            if q1:
                j = len(q1) - 1
                while j > 0 and q1[j] is None:
                    j -= 1
                q1 = q1[:j+1]
                j = 0
                while j < len(q1) and q1[j] is None:
                    j += 1
                q1 = q1[j:]
                max_l = max(max_l, len(q1))
                while q1:
                    now = q1.pop(0)
                    if now:
                        q2.append(now.left)
                        q2.append(now.right)
                    else:
                        q2.append(None)
                        q2.append(None)
                if list(set(q2)) == [None]:
                    break
            elif q2:
                j = len(q2) - 1
                while j > 0 and q2[j] is None:
                    j -= 1
                q2 = q2[:j+1]
                j = 0
                while j < len(q2) and q2[j] is None:
                    j += 1
                q2 = q2[j:]
                max_l = max(max_l, len(q2))
                while q2:
                    now = q2.pop(0)
                    if now:
                        q1.append(now.left)
                        q1.append(now.right)
                    else:
                        q1.append(None)
                        q1.append(None)
                if list(set(q1)) == [None]:
                    break
        return max_l

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = [(root, 0, 0)]
        current_depth = left = ans = 0
        while queue:
            node, pos, depth = queue.pop(0)
            if node:
                queue.append((node.left, pos * 2, depth + 1))
                queue.append((node.right, pos * 2+1, depth + 1))
                if current_depth != depth:
                    current_depth = depth
                    left = pos
                ans = max(pos-left+1, ans)
        return ans

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    left = root.left
    right = root.right
    left.left = TreeNode(1)
    left.left.left = TreeNode(1)
    right.right = TreeNode(1)
    right.right.right = TreeNode(1)
    s = Solution()
    s.widthOfBinaryTree(root)

