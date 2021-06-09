def get_max(now, arr):
    if not arr:
        return 1
    max_l = 1
    for i in range(len(arr)):
        if now[0] < arr[i][0] and now[1] < arr[i][1]:
            new_array = array[:i] + arr[i+1:]
            res = get_max(arr[i], new_array) + 1
            max_l = max(max_l, res)
    return max_l