class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        if k < 1:    # 注意判断输入的范围，防止越界
            return None
        if head is None:  # 注意判断输入是否为空
            return None
        stack = []
        while head is not None:
            stack.append(head)
            head = head.next
        if len(stack) < k: # 注意判断输入的范围，防止越界
            return None
        else:
            return stack[-k].val
