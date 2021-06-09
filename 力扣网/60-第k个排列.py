class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = 1
        for i in range(1, n):
            factorial *= i
        v = [str(i) for i in range(1, n+1)]
        s = ''
        carry = n-1
        while k > 0:
            a, b = divmod(k, factorial)
            if b == 0:
                now = v.pop(a-1)
                p = now + "".join(v[::-1])
                s += p
                return s
            else:
                now = v.pop(a)
                s += now
                factorial = factorial // carry
                carry -= 1
                k = b

if __name__ == '__main__':
    s = Solution()
    res = s.getPermutation(4, 1)
    print(res)
