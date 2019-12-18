class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if len(array)<2:
            return []
        if len(array) == 2:
            if array[0] == array[1]:
                return []
            else:
                return array

        result = []
        for a in array:
            if array.count(a) == 1:
                result.append(a)
                if len(result) == 2:
                    break
        return result