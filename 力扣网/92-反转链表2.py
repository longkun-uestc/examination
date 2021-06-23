# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre = None
        now = head
        m_copy = m
        while now and m > 1:
            pre = now
            now = now.next
            m -= 1
        q = now
        p = None
        while now and n-m_copy > 0:
            next = now.next
            now.next = p
            p = now
            now = next
            n -= 1
        if pre:
            pre.next = p
        q.next = now
        if pre:
            return head
        else:
            return p






