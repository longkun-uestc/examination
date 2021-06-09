class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        phead = None
        carry = 0
        first = True
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            res = x+y+carry
            carry = res // 10
            res = res % 10
            node = ListNode(res)
            if first:
                head = node
                phead = node
                first = False
            else:
                head.next = node
                head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return phead

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
    s1 = [2,4,3]
    s2 = [5, 6, 4]
    l1 = create_list(s1)
    l2 = create_list(s2)
    s = Solution()
    res = s.addTwoNumbers(l1, l2)
    show_list(res)

