class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if len(array) == 0:
            return 0
        F = array[0]
        res = array[0]
        for i in range(1, len(array)):
            F = max(F+array[i], array[i])
            res = max(res, F)
        return res
        # 这样也可以，但是要需要O(n)的空间复杂度
        # F = [array[0]]
        # res = array[0]
        # for i in range(1, len(array)):
        #     F.append(max(F[i-1] + array[i], array[i]))
        #     res = max(res, F[i])
        # return res