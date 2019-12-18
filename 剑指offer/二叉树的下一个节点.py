class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        if pNode is None:
            return None
        if pNode.right is not None:
            pNode = pNode.right
            while pNode.left is not None:
                pNode = pNode.left
            return pNode
        if pNode.next is not None and pNode.next.left is pNode:
            return pNode.next
        if pNode.next is not None:
            while pNode.next is not None and pNode.next.right is pNode:
                pNode = pNode.next
            return pNode.next
        return None
