class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 is None or pHead2 is None:
            return None
        while pHead1 is not None:
            now = pHead2
            while now is not None:
                if pHead1 is now:
                    return now
                else:
                    now = now.next
            pHead1 = pHead1.next
        return None
