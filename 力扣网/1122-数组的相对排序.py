from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i = 0
        for x in arr2:
            for j in range(i, len(arr1)):
                if arr1[j] == x:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                    i += 1
        for k in range(i, len(arr1)):
            for j in range(k+1, len(arr1)):
                if arr1[j] < arr1[k]:
                    arr1[k], arr1[j] = arr1[j], arr1[k]
        return arr1

if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 19, 9, 2, 7]
    arr2 = [2, 1, 4, 3, 9, 6]
    s = Solution()
    R = s.relativeSortArray(arr1, arr2)
    print(R)