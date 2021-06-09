class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx = len(s)-1
        res = 0
        while idx >= 0 and s[idx] == " ":
            idx -= 1
        while idx >= 0 and s[idx] != " ":
            res += 1
            idx -= 1
        return res

if __name__ == '__main__':
    x = "    adgre   c "
    s = Solution()
    r = s.lengthOfLastWord(x)
    print(r)