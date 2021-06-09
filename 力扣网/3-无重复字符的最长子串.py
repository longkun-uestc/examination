class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        max_l = 1
        for r in range(2, len(s)+1):
            for i in range(len(s)-r+1):
                j = i + r - 1
                p1,p2 = 0,0
                if dp[i][j-1] == len(s[i:j]) and s[j] not in s[i:j]:
                    p1 = dp[i][j-1]+1
                if dp[i+1][j] == len(s[i+1:j+1]) and s[i] not in s[i+1:j+1]:
                    p2 = dp[i+1][j] + 1
                dp[i][j] = max(p1, p2, dp[i][j-1], dp[i+1][j])
                max_l = max(max_l, dp[i][j])
        # for d in dp:
        #     print(d)
        # print(max_l)
        return max_l

    def lengthOfLongestSubstring1(self, s: str) -> int:
        i = 0
        max_l = 0
        while i < len(s):
            j = i + 1
            index_dic = {s[i]: i}
            while j < len(s) and s[j] not in index_dic:
                index_dic[s[j]] = j
                j += 1
            max_l = max(max_l, j-i)
            if j < len(s):
                i = index_dic[s[j]]+1
            else:
                break
        return max_l

    def lengthOfLongestSubstring2(self, s: str) -> int:
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans

    def lengthOfLongestSubstring3(self, s: str) -> int:
        i = 0
        j = 1
        max_l = 1
        index_dic = {s[0]:0}
        while i < len(s):
            while j < len(s) and s[j] not in index_dic:
                index_dic[s[j]] = j
                j += 1
            max_l = max(max_l, j-i)
            if j < len(s):
                new_i = index_dic[s[j]] + 1
                for k in range(i, new_i):
                    index_dic.pop(s[k])
                i = new_i
            else:
                break
        return max_l
if __name__ == '__main__':
    s = "pwwkew"
    s = "abcabcbb"
    a = Solution()
    a.lengthOfLongestSubstring3(s)

