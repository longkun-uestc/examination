if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        dis = 0
        i = 0
        while i < len(arr):
            while i< len(arr)-1 and arr[i] <= arr[i+1]:
                i += 1
            cnt = 1
            j = i+1
            while j < len(arr) and arr[j] < arr[j-1]:
                j += 1
                cnt += 1
            if j < len(arr) and arr[j] == arr[j-1]:
                k = j + 1
                cnt1 = 1
                while k < len(arr) and arr[k] > arr[k-1]:
                    k += 1
                    cnt1 += 1
                if cnt1 >= cnt:
                    dis = max(dis, cnt*2)
                i = k - 1
            else:
                i = j
        print(dis)




