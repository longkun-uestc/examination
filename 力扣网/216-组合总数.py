from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        def dfs(k , n, arr, tmp):
            if k == 0 and n == 0:
                self.res.append(tmp[:])
                return
            for i, x in enumerate(arr):
                if x <= n:
                    new_tmp = tmp[:]
                    new_tmp.append(x)
                    dfs(k-1, n-x, arr[i+1:], new_tmp)
        dfs(k, n, [i+1 for i in range(8)], [])
        return self.res

if __name__ == '__main__':
    s = Solution()
    r = s.combinationSum3(3, 15)
    print(r)