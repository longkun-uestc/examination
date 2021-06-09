from typing import List
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        dp = [[[0 for i in range(len(boxes))]for j in range(len(boxes))] for k in range(len(boxes))]
        for i in range(len(boxes)):
            # dp[i][i][0] = 1
            for k in range(len(boxes)):
                dp[i][i][k] = (k+1)**2

        for r in range(2, len(boxes)+1):
            for i in range(len(boxes)-r+1):
                j = i + r - 1
                for k in range(0, len(boxes)-j):
                    # print(i, j, k)
                    x = dp[i][j-1][0] + (k+1)**2
                    tmp = [dp[i][m][k+1]+dp[m+1][j-1][0] for m in range(i, j) if boxes[m] == boxes[j]]
                    dp[i][j][k] = max(x, 0 if not tmp else max(tmp))
        return dp[0][len(boxes)-1][0]

if __name__ == '__main__':
    s = Solution()
    x = [1,3,2,2,2,3,4,3,1]
    x = [12,32,47,58,5,27,13,20,49,26,36,34,17,47,32,4,1,32,51,77,58,69,87,96,53,16,66,32,41,72,78,9,52,96,51,78,69,90,2,96,38,10,63,66,21,47,75,29,52,68,30,38,94,91,89,8,36,36,33,42,32,75,23,25,64,7,80,44,15,41,46,92,24,78,91,89,28,14,44,24,31,91,81,5,50,41,41,48,61,31,39,80,41,6,86,80,73,85,58,44]
    x = [85,29,31,29,98,77,76,91,67,47,15,10,11,82,79,28,86,47,88,37,99,22,79,98,10,41,86,58,12,53,80,3,5,82,88,61,88,66,64,86,57,58,98,3,6,24,30,31,74,1,58,57,70,23,100,2,82,3,1,35,97,78,74,59,100,89,67,12,76,83,23,59,62,18,60,76,47,2,56,25,95,64,63,94,49,14,60,3,43,65,62,68,86,4,62,49,75,72,70,63]
    res = s.removeBoxes(x)
    print(res)



