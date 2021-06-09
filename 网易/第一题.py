from collections import defaultdict
def check(A, map_dict):
    l = []
    max_key = -1
    for key, val in map_dict.items():
        if val > 0:
            max_key = max(max_key, key)
            
    return True if str(max_key) > A[0] else False

if __name__ == '__main__':
    N = int(input())
    A = input()
    B = input()
    map_dict = defaultdict(int)
    for b in B:
        map_dict[int(b)] += 1
    i = 0
    cnt = ""
    s = []
    while i < len(A):
        if not check(A[i:], map_dict):
            if not s:
                break
            c = s.pop(-1)
            map_dict[c] += 1
            i -= 1
            next_c = ''
            for x in range(c+1, 10):
                if map_dict[x] > 0:
                    next_c = x
                    break
            map_dict[next_c] -= 1
            s.append(next_c)
            l = []
            for key, val in map_dict.items():
                l.extend([str(key)] * val)
            l.sort()
            s.extend(l)
            break
        else:
            c = A[i]
            next_c = ''
            for x in range(int(c), 10):
                if map_dict[x] > 0:
                    next_c = x
                    break
            if next_c == c:
                s.append(next_c)
                map_dict[next_c] -= 1
                i += 1
            else:
                map_dict[next_c] -= 1
                s.append(next_c)
                l = []
                for key, val in map_dict.items():
                    l.extend([str(key)] * val)
                l.sort()
                s.extend(l)
                break
    if not s:
        print(-1)
    else:
        print(''.join(map(str, s)))








