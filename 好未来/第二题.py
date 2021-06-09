class Solution:
    def minDistance(self, word1, word2):
        dp = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
        for i in range(1, len(word2) + 1):
            dp[0][i] = i
        for i in range(1, len(word1) + 1):
            dp[i][0] = i
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
        # for d in dp:
        #     print(d)
        return dp[len(word1)][len(word2)]


if __name__ == '__main__':
    s = Solution()
    w1 = 'kitten'
    w2 = 'sittin'
    s.minDistance(w1, w2)
