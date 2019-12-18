class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        stack = []
        if listNode == None:
            return []
        stack.append(listNode.val)
        while listNode.next != None:
            listNode = listNode.next
            stack.append(listNode.val)
        s = []
        while stack:
            s.append(stack.pop())
        return s