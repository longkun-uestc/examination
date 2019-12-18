class Solution:
    def IsPopOrder(self, pushV, popV):
        if len(pushV) != len(popV):
            return False
        support_stack = []
        while len(pushV) > 0:
            a = pushV.pop(0)
            if a != popV[0]:
                support_stack.append(a)
            else:
                popV.pop(0)
                if len(popV) == 0:
                    break
                while popV[0] == support_stack[-1]:
                    popV.pop(0)
                    support_stack.pop()
                    if len(support_stack) == 0:
                        break
        if len(support_stack) == 0:
            return True
        else:
            return False
