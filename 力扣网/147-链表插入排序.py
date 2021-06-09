class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        phead = ListNode(-1)
        phead.next = head
        next = head.next
        next_pre = head
        while next:
            pre, now = phead, phead.next
            while now.val < next.val:
                pre = now
                now = now.next
            if now == next:
                next_pre = next
                next = next.next
            else:
                next_pre.next = next.next
                next.next = now
                pre.next = next
                next = next_pre.next
                show_list(phead)
        return phead.next

def create_list(s):
    head = ListNode(s[0])
    last = head
    for i in range(1, len(s)):
        now = ListNode(s[i])
        last.next = now
        last = now
    return head


def show_list(head):
    arr = []
    while head is not None:
        arr.append(head.val)
        head = head.next
    print(arr)

if __name__ == '__main__':
    s = [2,1]
    head = create_list(s)
    sol = Solution()
    res = sol.insertionSortList(head)
    show_list(res)


