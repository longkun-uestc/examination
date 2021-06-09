class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        seq = [0, 1]
        res = []
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                seq[1] += 1
            else:
                res.append(min(seq))
                seq[0] = seq[1]
                seq[1] = 1
            print(s[i], seq, res)
        res.append(min(seq))
        return sum(res)

if __name__ == '__main__':
    s = Solution()
    x = "1110010000"
    r = s.countBinarySubstrings(x)
    print(r)