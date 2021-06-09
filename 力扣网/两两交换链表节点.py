class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = None
        next = None
        first = True
        phead = None
        while head and head.next:
            next = head.next
            head.next = next.next
            next.next = head
            if first:
                phead = next
                first = False
            else:
                pre.next = next
            pre = head
            head = head.next
        if first:
            phead = head
        return phead


def create_list(s):
    if not s:
        return None
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
    s = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7]
    s = []
    head = create_list(s)
    show_list(head)
    solution = Solution()
    phead = solution.swapPairs(head)
    show_list(phead)


