class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        C = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        for i in range(1, len(word1)+1):
            C[i][0] = i
        for j in range(1, len(word2)+1):
            C[0][j] = j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    C[i][j] = C[i-1][j-1]
                else:
                    C[i][j] = min(C[i-1][j]+1, C[i][j-1]+1, C[i-1][j-1]+1)

        return C[len(word1)][len(word2)]