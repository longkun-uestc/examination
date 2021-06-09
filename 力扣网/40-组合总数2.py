from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []
        res = []
        path = []
        candidates.sort()
        self.dfs(candidates, target, 0, size, path, res)
        return res

    def dfs(self, candidates, target, start, size, path, res):
        if target == 0:
            res.append(path[:])
        for idx in range(start, size):
            if idx > start and candidates[idx] == candidates[idx-1]:
                continue
            residue = target - candidates[idx]
            if residue < 0:
                break
            path.append(candidates[idx])
            self.dfs(candidates, residue, idx+1, size, path, res)
            path.pop()

if __name__ == '__main__':
    s = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    candidates = [4,4,2,1,4,2,2,1,3]
    candidates.sort()
    print(candidates)
    target = 6
    s.combinationSum2(candidates, target)