class Solution:
    def Power(self, base, exponent):
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        all = 1
        num = exponent if exponent > 0 else -exponent
        for i in range(num):
            all *= base
        return all if exponent > 0 else 1/all
        # 这样也可以
        # return base**(exponent)


if __name__ == '__main__':
    s = Solution()
    a = s.Power(2, -4)
    print(a)
