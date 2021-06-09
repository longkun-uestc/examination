import math
def get_jie(a, b, c):
    delta = b**2-4*a*c
    if delta < 0:
        return []
    else:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        if x1 == x2:
            return [x1]
        else:
            return sorted([x1, x2])
def get_res(x, param):
    res = 0
    exp = len(param)-1
    for idx, p in enumerate(param):
        res += p * x ** (exp-idx)
    return res

def get_gen(pos, param):
    pos = [-10000000000] + pos +[10000000000]
    jie = []
    for i in range(len(pos)-1):
        x1 = get_res(pos[i], param)
        x2 = get_res(pos[i+1], param)
        if x1 == 0:
            jie.append(pos[i])
            continue
        if x1 < 0 and x2 <= 0 or x1 > 0 and x2 >= 0:
            continue
        else:
            p1, p2 = pos[i], pos[i+1]
            while abs(p1-p2) > 0.001:
                mid = (p1+p2)/2
                x = get_res(mid, param)
                if x1 * x > 0:
                    p1 = mid
                else:
                    p2 = mid
            jie.append(p1)
    return jie

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    while a[0] == 0:
        a.pop(0)
        n -= 1
    p = n
    dif = a.copy()
    while p > 2:
        for i in range(p):
            dif[i] = dif[i] * (p-i)
        dif = dif[:-1]
        p -= 1
    res = get_jie(dif[0], dif[1], dif[2])
    m = 2
    while m < n:
        param = a.copy()
        q = n
        while q > m+1:
            for i in range(q):
                param[i] = param[i] * (q - i)
            param = param[:-1]
            q -= 1
        res = get_gen(res, param)
        m += 1
    # print(res)
    if not res:
        print("No")
    else:
        new_res = []
        for r in res:
            if abs(r-0) < 0.001:
                new_res.append(0)
            else:
                new_res.append(r)
        r = ["{:.2f}".format(x) for x in new_res]
        s = " ".join(r)
        print(s)


