class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        result = []
        for n in range(2, tsum):
            a1 = tsum / n - n / 2 + 1 / 2
            a2 = int(a1)
            if a1 > 0 and (a1-a2) == 0:
                L = [int(a1 + i) for i in range(n)]
                result.append(L)
        result.sort(key=lambda val: val[0])
        return result

    # def FindContinuousSequence(self, tsum):
    #     if tsum < 3:
    #         return []
    #     result = []
    #     for i in range(1, tsum//2+1):
    #         t = i
    #         for j in range(i+1, tsum):
    #             t += j
    #             if t == tsum:
    #                 L = [k for k in range(i, j+1)]
    #                 result.append(L)
    #                 break
    #             elif t > tsum:
    #                 break
    #     result.sort(key=lambda val: val[0])
    #     # print(result)
    #     return result



if __name__ == '__main__':
    s = Solution()
    s.FindContinuousSequence(4)
