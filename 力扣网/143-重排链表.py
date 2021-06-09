class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        fast = low = head
        # phead = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            low = low.next
        new_head = low.next
        low.next = None
        pre, next = None, None
        while new_head:
            next = new_head.next
            new_head.next = pre
            pre = new_head
            new_head = next
        head1 = pre
        while head and head1:
            next = head.next
            head.next = head1
            head1 = head1.next
            # head = head.next
            # head.next = next
            # head = head.next
            head.next.next = next
            head = next
        # return phead

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
    s = [1, 5]
    head = create_list(s)
    solution = Solution()
    show_list(head)
    res = solution.reorderList(head)
    show_list(res)
    
