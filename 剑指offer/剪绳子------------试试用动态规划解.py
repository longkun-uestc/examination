import math


def compute_max(n, k):
    length = n / float(k)
    if length % 1 == 0:
        return (n / k) ** k
    else:
        floor = math.floor(length)
        b = n - k * floor
        a = k - n + k * floor
        return floor**a * (floor+1)**b


class Solution:
    def cutRope(self, number):
        max_num = -1
        for i in range(2, number+1):
            mul = compute_max(number, i)
            if mul > max_num:
                max_num = mul
        return max_num


if __name__ == '__main__':
    s = Solution()
    s.cutRope(3)

