class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        stack = []
        phead = head
        while phead:
            stack.append(phead)
            phead = phead.next
        i = 0
        node = None
        while i < n:
            node = stack.pop()
            i += 1
        if stack:
            last = stack.pop()
            last.next = node.next
            del node
        else:
            head = head.next
            del node
        return head

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        phead = ListNode(-1)
        phead.next = head
        n1 = phead
        n2 = head
        i = 1
        while i < n and n2 is not None:
            n2 = n2.next
            i += 1

        while n2.next is not None:
            n2 = n2.next
            n1 = n1.next
        n1.next = n1.next.next
        return phead.next