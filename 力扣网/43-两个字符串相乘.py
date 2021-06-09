class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        res = '0'
        cnt = ""
        for j in range(len(num2)-1, -1, -1):
            s = self.mul_1(num1, num2[j])
            s = s + cnt
            res = self.add(res, s)
            cnt += "0"
        return res



    def mul_1(self, num1, c):
        s = ""
        i = len(num1) - 1
        cnt = 0
        while i >=0 or cnt > 0:
            x = int(num1[i]) if i >=0 else 0
            y = int(c) * x + cnt
            cnt = y // 10
            y = y % 10
            s = str(y) + s
            i -= 1
        return s

    def add(self, s1, s2):
        s = ''
        cnt = 0
        i = len(s1)-1
        j = len(s2)-1
        while i >= 0 or j >= 0 or cnt > 0:
            x = int(s1[i]) if i >= 0 else 0
            y = int(s2[j]) if j >= 0 else 0
            z = x + y + cnt
            cnt = z // 10
            z = z % 10
            s = str(z) + s
            i -= 1
            j -= 1
        return s

if __name__ == '__main__':
    s = Solution()
    s1 = '123'
    s2 = '10'
    x = s.multiply(s1, s2)
    print(x)
