def gcd(a, b):
    if a < b:
        tmp = a
        a = b
        b = tmp
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def argsort(array):
    s = sorted(array)
    result = []
    for i, a in enumerate(array):
        if a == s[0]:
            result.append(i)
            break
    for i, a in enumerate(array):
        if a == s[1] and i != result[0]:
            result.append(i)
            break
    result.append(list(set([0, 1, 2]).difference(set(result)))[0])
    return result


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        now = [a, b, c]
        increase = [a, b, c]
        num = 1
        ugly = min(now)
        while num <= n:
            ugly = min(now)
            index = argsort(now)
            print(now, index, num, ugly)
            # if now[index[0]] == now[index[1]]:
            #     if now[index[1]] == now[index[2]]:
            #         now[index[0]] += increase[index[0]]
            #         now[index[1]] += increase[index[1]]
            #         now[index[2]] += increase[index[2]]
            #     else:
            #         now[index[0]] += increase[index[0]]
            #         now[index[1]] += increase[index[1]]
            #     num += 1
            # else:
            count = (now[index[1]] - now[index[0]]) // increase[index[0]]
            if num + count >= n:
                print("equal return")
                return now[index[0]] + (n - num) * increase[index[0]]
            else:
                if (now[index[1]] - now[index[0]]) % increase[index[0]] == 0:
                    if now[index[2]] == now[index[1]]:
                        now[index[2]] += increase[index[2]]
                    now[index[0]] += (count + 1) * increase[index[0]]
                    now[index[1]] += increase[index[1]]
                else:
                    now[index[0]] += (count + 1) * increase[index[0]]
                num = num + count + 1





if __name__ == '__main__':
    s = Solution()
    n = 1000000000
    a = 2
    b = 217983653
    c = 336916467
    # a = 2
    # b = 4
    # c = 100
    # n = 51
    # n = 5
    # a = 2
    # b = 11
    # c = 13
    # n = 4
    # a = 2
    # b = 3
    # c = 4
    # n = 3
    # a = 2
    # b = 3
    # c = 5
    a = s.nthUglyNumber(n, a, b, c)
    print("---------------")
    print(a)
