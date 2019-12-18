class ListNode:
    def __init__(self, x):
        self.val = x
        # self.is_check = False
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        if pHead is None:
            return None
        node_list = []
        while pHead is not None:
            # for n in node_list:
            #     if pHead is n:
            #         return pHead
            if pHead in node_list:
                return pHead
            else:
                node_list.append(pHead)
            pHead = pHead.next
        return None
