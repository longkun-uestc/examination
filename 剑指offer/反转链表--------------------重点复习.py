class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        pre = None
        next = None
        while pHead:
            next = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = next
        return pre
        # stack = []
        # while pHead:
        #     stack.append(pHead)
        #     pHead = pHead.next
        # new_head = stack.pop()
        # now = new_head
        # for i in range(len(stack)-1, -1, -1):
        #     now.next = stack[i]
        #     now = now.next
        # return new_head

