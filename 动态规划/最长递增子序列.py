
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

    def findLongest1(self, A, n):
        if len(A) == 0:
            return 0
        ends = [A[0]]
        dp = [1] * n
        for i in range(1, n):
            print(ends)
            l, r = (0, len(ends) - 1)
            while l <= r:
                mid = (l + r) // 2
                if A[i] < ends[mid]:
                    r = mid - 1
                elif A[i] == ends[mid]:
                    l = mid
                    break
                else:
                    l = mid + 1
            if l < len(ends):
                ends[l] = A[i]
            else:
                ends.append(A[i])
            dp[i] = l + 1
        # print("---------")
        # print(ends)
        # print(dp)
        # print(max(dp))
        return max(dp)


if __name__ == '__main__':
    s = AscentSequence()
    x = [2, 2, 4, 3, 1, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # x = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    s.findLongest1(x, 14)
