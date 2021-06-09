map_dict = {}
def dfs(arr):
    if len(arr) == 0:
        return 1
    if len(arr) == 1:
        return 1
    cnt = 0
    for i, x in enumerate(arr):
        left_arr = arr[:i]
        right_arr = arr[i+1:]
        if tuple(left_arr) not in map_dict:
            left_cnt = dfs(left_arr)
        else:
            left_cnt = map_dict[tuple(left_arr)]
        if tuple(right_arr) not in map_dict:
            right_cnt = dfs(right_arr)
        else:
            right_cnt = map_dict[tuple(right_arr)]
        cnt += left_cnt*right_cnt
    map_dict[tuple(arr)] = cnt
    return cnt


if __name__ == '__main__':
    n = int(input())
    if n == 0:
        print(0)
    else:
        arr = [i+1 for i in range(n)]
        res = dfs(arr)
        print(res)