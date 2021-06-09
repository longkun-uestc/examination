from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        node_list = []
        phead = ListNode(-1)
        head = phead
        for node in lists:
            if node is not None:
                node_list.append(node)
        node_list.sort(key=lambda x: x.val)
        idx = 0
        while idx < len(node_list)-1:
            node = node_list[idx]
            # if node is None:
            #     idx += 1
            #     continue
            head.next = node
            pre = None
            while node and node.val <= node_list[idx+1].val:
                pre = node
                node = node.next
            head = pre
            node_list[idx] = node
            if node is None:
                idx += 1
            else:
                j = idx + 1
                while j < len(node_list) and node_list[j].val < node_list[j-1].val:
                    node_list[j], node_list[j-1] = node_list[j-1], node_list[j]
                    j += 1
        head.next = node_list[-1]
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
    s1 = create_list( [1,4,5])
    s2 = create_list([1,3,4])
    s3 = create_list([2,6])
    s = Solution()
    res = s.mergeKLists([s1, s2, s3])
    show_list(res)

