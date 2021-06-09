from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = self.get_ip(s, 4)
        new_res = []
        for r in res:
            x = '.'.join(r)
            new_res.append(x)
        print(new_res)
        return new_res

    def get_ip(self, str, count):
        res = []
        if count == 1:
            if str and int(str)<256:
                if str[0] == '0' and len(str) > 1:
                    res.append([])
                else:
                    res.append([str])
            else:
                res.append([])
            return res
        else:
            for i in range(min(len(str), 3)):
                if int(str[:i+1]) < 256:
                    if str[:i+1][0] == '0' and len(str[:i+1]) > 1:
                        continue
                    sub_res = self.get_ip(str[i+1:], count-1)
                    for sub in sub_res:
                        if sub:
                            new = [str[:i + 1]] + sub
                            res.append(new)
            return res

if __name__ == '__main__':
    s = Solution()
    x = "25525511135"
    x = '11112'
    x = '00102'
    x = '101010'
    res = s.restoreIpAddresses(x)



