class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend < -2**31:
                return 2**31-1
            else:
                return -dividend
        if dividend >= 0 and divisor > 0 or dividend < 0 and divisor < 0:
            flag = False
        else:
            flag = True
        divisor = abs(divisor)
        dividend = abs(dividend)
        cnt = self.div(dividend, divisor)
        if flag:
            cnt = -cnt
        if cnt > 2**31-1:
            cnt = 2**31-1
        if cnt < -2**31:
            cnt = -2**31
        return cnt

    def div(self, a, b):
        if a < b:
            return 0
        count = 1
        c = b
        while (c + c) <= a:
            count = count + count
            c = c + c
        return count + self.div(a-c, b)

if __name__ == '__main__':
    s = Solution()
    r = s.divide(-20, -1)
    print(r)