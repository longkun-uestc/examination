def min_dis(mat, end):
    visited = set()
    now = 0
    stack = [now]
    dis_dict = {(0, 0): 0}
    while stack:
        now = stack.pop(0)
        if now in visited:
            continue
        for idx, t in enumerate(mat[now]):
            if t != -1:
                now_dis = dis_dict.get((0, idx), 100000000000)
                dis_dict[(0, idx)] = min(now_dis, dis_dict[(0, now)] + t)
                if idx in visited and now_dis != dis_dict[(0, idx)]:
                    visited.remove(idx)
                if idx not in visited and idx not in stack:
                    stack.append(idx)
        visited.add(now)
    return dis_dict[(0, end)]

if __name__ == '__main__':
    N, P = list(map(int, input().split()))
    mat = [[-1 for i in range(N)] for j in range(N)]
    for i in range(P):
        s, e, t = list(map(int, input().split()))
        mat[s][e] = t
        mat[e][s] = t
    end = int(input())
    res = min_dis(mat, end)
    print(res)
# 4 5
# 0 1 15
# 1 2 15
# 0 3 50
# 1 3 30
# 2 3 10
# 3