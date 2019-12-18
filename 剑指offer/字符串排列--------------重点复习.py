def find(ss):
    if len(ss) == 0:
        return None
    if len(ss) == 1:
        return ss
    else:
        result = []
        for i in range(0, len(ss)):
            if i == 0 or ss[i] != ss[0]:
                tmp = ss[i]
                ss[i] = ss[0]
                ss[0] = tmp
                new_result = find(ss[1:])
                for new in new_result:
                    new = ss[0] + new
                    result.append(new)
                tmp = ss[i]
                ss[i] = ss[0]
                ss[0] = tmp
        return result
class Solution:
    def Permutation(self, ss):
        if len(ss) == 0:
            return []
        else:
            ss = list(ss)
            result = find(ss)
            result.sort()
            return result

if __name__ == '__main__':
    s = Solution()
    x = "12345"
    x = "abc"
    a = s.Permutation(x)
    print(a)
    print(type(a[0]))
