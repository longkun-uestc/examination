# def check(n):
#     while n != 1:
#         if n % 2 == 0:
#             n = n / 2
#         elif n % 3 == 0:
#             n = n / 3
#         elif n % 5 == 0:
#             n = n / 5
#         else:
#             break
#     if n == 1:
#         return True
#     else:
#         return False

class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        result = [1]
        (p2, p3, p5) = (0, 0, 0)
        for i in range(1, index):
            result.append(min(result[p2] * 2, result[p3] * 3, result[p5] * 5))
            if result[i] == result[p2] * 2:
                p2 += 1
            if result[i] == result[p3] * 3:
                p3 += 1
            if result[i] == result[p5] * 5:
                p5 += 1
        return result[-1]


if __name__ == '__main__':
    s = Solution()
    s.GetUglyNumber_Solution(10)
