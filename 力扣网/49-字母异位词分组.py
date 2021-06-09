from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            st = "".join(sorted(s))
            if st not in d:
                d[st] = [s]
            else:
                d[st].append(s)
        res = []
        for k, v in d.items():
            res.append(v)
        return res

if __name__ == '__main__':
    a = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    r = s.groupAnagrams(a)
    print(r)