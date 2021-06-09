def get_min(arr, K):
    if K == 0:
        return
    i = 0
    while i < len(arr)-1 and arr[i] <= arr[i+1]:
        i += 1
    arr.pop(i)
    get_min(arr, K-1)

if __name__ == '__main__':
    s = input()
    K = int(input())
    arr = list(s)
    get_min(arr, K)
    res = ''.join(arr)
    i = 0
    while i < len(res) and res[i] == '0':
        i += 1
    res = res[i:]
    if not res:
        print("0")
    else:
        print(res)
