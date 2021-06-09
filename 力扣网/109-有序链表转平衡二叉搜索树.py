class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def get_mid(left, right):
            fast = low = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                low = low.next
            return low

        def build_tree(left, right):
            if left == right:
                return None
            mid = get_mid(left, right)
            root = TreeNode(mid.val)
            root.left = build_tree(left, mid)
            root.right = build_tree(mid.next, right)
            return root
        return build_tree(head, None)