
class AscentSequence:
    def findLongest(self, A, n):
        if len(A) == 0:
            return 0
        dp = [1] * n
        for i in range(1, len(A)):
            max_dp = 0
            for j in range(0, i):
                if A[j] < A[i] and dp[j] > max_dp:
                    max_dp = dp[j]
            dp[i] = max_dp + 1
        print(dp)
        return max(dp)


if __name__ == '__main__':
    s = AscentSequence()
    x = [2, 1, 4, 3, 1, 5, 6]
    s.findLongest(x, 7)
