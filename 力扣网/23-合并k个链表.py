from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        now_list = []
        phead = ListNode(-1)
        head = phead
        for node in lists:
            now_list.append(node)
        while self.check_all(now_list):
            print(now_list)
            min_node = ListNode(100000000)
            idx = -1
            for i, node in enumerate(now_list):
                if node is not None:
                    if node.val < min_node.val:
                        min_node = node
                        idx = i
            head.next = min_node
            head = head.next
            now_list[idx] = now_list[idx].next
        return phead.next

    def check_all(self, now_list):
        for node in now_list:
            if node is not None:
                return True
        return False
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
    s1 = create_list( [1,4,5])
    s2 = create_list([1,3,4])
    s3 = create_list([2,6])
    s = Solution()
    res = s.mergeKLists([s1, s2, s3])
    show_list(res)

