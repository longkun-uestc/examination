class Solution:
    stack = []
    min_element = None

    def push(self, node):
        if len(self.stack) == 0:
            self.min_element = node
        elif node < self.min_element:
            self.min_element = node
        self.stack.append(node)
        # write code here

    def pop(self):
        if len(self.stack) == 0:
            raise Exception("empty stack")
        else:
            s = self.stack.pop()
            if len(self.stack) == 0:
                self.min_element = None
            elif s <= self.min_element:
                self.min_element = min(self.stack)
            return s

        # write code here

    def top(self):
        return self.stack[-1]
        # write code here

    def min(self):
        if len(self.stack) == 0:
            raise Exception("empty stack")
        else:
            return self.min_element

# 第二种写法，第一种写法贼傻逼
class Solution:
    stack = []
    def push(self, node):
        self.stack.append(node)
        # write code here
    def pop(self):
        if len(self.stack) == 0:
            raise Exception("empty stack")
        else:
            return self.stack.pop()
        # write code here
    def top(self):
        return self.stack[-1]
        # write code here
    def min(self):
        return min(self.stack)
