class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) == 0 or len(tinput) < k:
            # raise Exception("index out of range")
            return []
        tinput.sort()
        return tinput[:k]