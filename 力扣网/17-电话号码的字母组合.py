from typing import List
class Solution:
    map_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    s = ''
    res = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        # res = self.get_arr(digits)
        self.get_arr1(digits, 0)
        return self.res

    def get_arr(self, digits):
        if not digits:
            return ['']
        s = self.map_dict[digits[0]]
        arr = self.get_arr(digits[1:])
        res = []
        for c in s:
            for a in arr:
                res.append(c+a)
        return res
    def get_arr1(self, digits, idx):
        if idx == len(digits):
            self.res.append(self.s)
            return
        for c in self.map_dict[digits[idx]]:
            self.s = self.s + c
            self.get_arr1(digits, idx+1)
            self.s = self.s[:-1]

if __name__ == '__main__':
    s = Solution()
    d = '2'
    r = s.letterCombinations(d)
    print(r)
