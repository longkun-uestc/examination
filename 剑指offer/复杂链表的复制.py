class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead is None:
            return None
        nodes = []
        random_nodes = []
        head_copy = pHead
        while head_copy is not None:
            nodes.append(RandomListNode(head_copy.label))
            if head_copy.random is None:
                random_nodes.append(-1)
            else:
                ids = 0
                head = pHead
                while head:
                    if head is head_copy.random:
                        break
                    else:
                        ids += 1
                        head = head.next
                random_nodes.append(ids)
            head_copy = head_copy.next
        head = nodes[0]
        now = head
        if random_nodes[0] == -1:
            head.random = None
        else:
            head.random = nodes[random_nodes[0]]
        for i in range(1, len(random_nodes)):
            now.next = nodes[i]
            now = now.next
            if random_nodes[i] == -1:
                now.random = None
            else:
                now.random = nodes[random_nodes[i]]
        return head



        # new_head = None
        # now = None
        # random = None
        # now_val = pHead.label
        # now = RandomListNode(now_val)
        # new_head = now

