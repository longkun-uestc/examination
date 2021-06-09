class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        num_col = (len(s) // (numRows+numRows-2))*(numRows-1) + 1
        mat = [['' for i in range(num_col)] for j in range(numRows)]
        i = 0
        n = 0
        m = 0
        direction = 'd'
        while i < len(s):
            if direction == 'd':
                mat[n][m] = s[i]
                n += 1
            else:
                mat[n][m] = s[i]
                n -= 1
                m += 1
            if n == numRows:
                direction = 't'
                n = n-2
                m += 1
            elif n == -1:
                direction = 'd'
                n = n + 2
                m -= 1
            i += 1
        for m in mat:
            print(m)
        s = ''
        for m in mat:
            s += ''.join(m)
        print(s)
        return s

    def convert1(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        m = len(s) // (numRows+numRows - 2) + 1
        print(m)
        all_s = ''
        for i in range(numRows):
            sub_s = s[i]
            for k in range(1, m + 1):
                idx = k*(numRows+numRows-2)-i
                # if 0 < idx < k*(numRows+numRows-2) and (k-1)*(numRows+numRows-2)+idx < len(s):
                #     sub_s += s[(k-1)*(numRows+numRows-2)+idx]
                if (k-1)*(numRows+numRows-2)+(numRows-1) < idx < k*(numRows+numRows-2) and idx < len(s):
                    sub_s += s[idx]
                if k*(numRows+numRows-2) + i < len(s):
                    sub_s += s[k*(numRows+numRows-2)+i]
            all_s += sub_s
        print(all_s)
        return all_s

    def convert2(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)




if __name__ == '__main__':
    s = Solution()
    s1 = "LEETCODEISHIRING"
    s2 = "ABCDE"
    s3 = 'A'
    s.convert1(s3, 2)
