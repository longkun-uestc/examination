class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        phead = ListNode(-1)
        phead.next = head
        j, ou = head, head.next
        nj = ou.next
        while ou and nj:
            ou.next = nj.next
            nj.next = j.next
            j.next = nj
            j = nj
            ou = ou.next
            if ou:
                nj = ou.next
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
    s = Solution()
    arr = [1,2,3,4,5,6]
    head = create_list(arr)
    head = s.oddEvenList(head)
    show_list(head)

