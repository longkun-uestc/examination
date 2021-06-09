from typing import List
class Solution:
    map_dict = {}
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.map_dict = {}
        self.get_arr(candidates, target)
        print(self.map_dict)
        return self.map_dict.get(target, [])

    def get_arr(self, candidates, target):
        if target == 0:
            return [[]]
        if target < candidates[0]:
            return []
        if target in self.map_dict:
            return self.map_dict[target]
        new_res = []
        for x in candidates:
            if x <= target:
                res = self.get_arr(candidates, target-x)
                if res:
                    for r in res:
                        new = r+[x]
                        new.sort()
                        if new not in new_res:
                            new_res.append(new)
        self.map_dict[target] = new_res
        return new_res

if __name__ == '__main__':
    s = Solution()
    candidates = [4,4,2,1,4,2,2,1,3]
    x = s.combinationSum(candidates, 6)
    print(x)