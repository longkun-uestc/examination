class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        if pHead1.val <= pHead2.val:
            head = ListNode(pHead1.val)
            pHead1 = pHead1.next
        else:
            head = ListNode(pHead2.val)
            pHead2 = pHead2.next
        now = head
        while pHead1 is not None and pHead2 is not None:
            if pHead1.val <= pHead2.val:
                now.next = ListNode(pHead1.val)
                now = now.next
                pHead1 = pHead1.next
            else:
                now.next = ListNode(pHead2.val)
                now = now.next
                pHead2 = pHead2.next
        if pHead1 is not None:
            now.next = pHead1
        if pHead2 is not None:
            now.next = pHead2
        return head
