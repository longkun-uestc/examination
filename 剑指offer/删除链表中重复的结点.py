class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        if pHead is None:
            return None
        now = pHead
        pre = None
        next = None
        while now is not None:
            # repeat = False
            next = now.next
            while next is not None and now.val == next.val:
                next = next.next
            if next is now.next:
                pre = now
                now = now.next
            else:
                if pre is None:
                    pHead = next
                    now = next
                else:
                    pre.next = next
                    now = next
        return pHead


if __name__ == '__main__':
    s = Solution()
    x = [1, 2, 3, 3, 4, 4, 5]
    x = [1,1,1,1,1,2,3,4,4,4,5,5]
    pHead = ListNode(x[0])
    now = pHead
    for i in range(1, len(x)):
        node = ListNode(x[i])
        now.next = node
        now = now.next
    head = s.deleteDuplication(pHead)
    a = []
    while head is not None:
        a.append(head.val)
        head = head.next
    print(a)
