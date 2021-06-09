from typing import List
class Solution:
    res = []
    stack = ['(']
    def generateParenthesis(self, n: int) -> List[str]:
        s = '('
        self.get(s, n-1)
        print(self.res)
        return self.res

    def get(self, s, n):
        if n == 0 and not self.stack:
            self.res.append(s)
            return
        if n > 0:
            self.stack.append('(')
            s += '('
            self.get(s, n-1)
            s = s[:-1]
            self.stack.pop()
        if self.stack:
            self.stack.pop()
            s += ')'
            self.get(s, n)
            s = s[:-1]
            self.stack.append('(')

if __name__ == '__main__':
    s = Solution()
    s.generateParenthesis(1)

