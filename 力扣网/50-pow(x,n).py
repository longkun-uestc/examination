class Solution:
    def myPow(self, x: float, n: int) -> float:
        def dfs(x, n):
            if n == 1:
                return x
            y = dfs(x, n//2)
            return y*y if n%2==0 else y*y*x
        if n == 0:
            return 1
        if n < 0:
            return 1/dfs(x, -n)
        else:
            return dfs(x, n)
if __name__ == '__main__':
    x = 2
    n = -2147483648
    s = Solution()
    r = s.myPow(x, n)
    print(r)
