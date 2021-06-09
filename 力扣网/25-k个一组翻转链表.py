# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        phead = None
        last_tag = None
        first = True
        while head is not None:
            count = 0
            check_head = head
            while count <= k and check_head is not None:
                count += 1
                check_head = check_head.next
            if count >= k:
                now_tag = head
                next = None
                pre = None
                num = k
                while num > 0:
                    next = head.next
                    head.next = pre
                    pre = head
                    head = next
                    num -= 1
                if first:
                    phead = pre
                    first = False
                else:
                    last_tag.next = pre
                last_tag = now_tag
            else:
                if first:
                    phead = head
                    first = False
                else:
                    last_tag.next = head
                break
        return phead

    def reverseKGroup1(self, head: ListNode, k: int) -> ListNode:
        phead = ListNode(-1)
        phead.next = head
        last_tag = phead
        while head is not None:
            count = 0
            next_head = head
            while count < k and next_head is not None:
                count += 1
                next_head = next_head.next
            if count == k:
                pre, next = None, None
                c = 0
                now_tag = head
                while c < k:
                    next = head.next
                    head.next = pre
                    pre = head
                    head = next
                    c += 1
                last_tag.next = pre
                now_tag.next = head
                last_tag = now_tag
            else:
                last_tag.next = head
                break
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
    s = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8]
    head = create_list(s)
    show_list(head)
    solution = Solution()
    phead = solution.reverseKGroup1(head, 7)
    show_list(phead)














