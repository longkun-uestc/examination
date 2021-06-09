
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    root = arr[0]
    level = 1
    left = 2**level - 1
    right = left + 2**level - 1
    left_arr = []
    right_arr = []
    while right < len(arr):
        left_arr.append(arr[left])
        right_arr.append(arr[right])
        level += 1
        left = 2 ** level - 1
        right = left + 2 ** level - 1
    # print(left_arr)
    # print(right_arr)
    leaf = []
    for i in range(left, len(arr)):
        leaf.append(arr[i])
    last_idx = len(arr)//2
    for i in range(last_idx, left):
        leaf.append(arr[i])
    #print(leaf)
    res = [root]
    res = res + left_arr + leaf[:-1] + right_arr[::-1]
    s = ' '.join(map(str, res))
    print(s)

