class Solution:
    l1 = []
    l2 = []
    def push(self, node):
        # write code here
        self.l1.append(node)
    def pop(self):
        if len(self.l1) == 0 and len(self.l2) == 0:
            return None
        if len(self.l2) == 0:
            while len(self.l1) != 0:
                self.l2.append(self.l1.pop())
        return self.l2.pop()

        # return xx