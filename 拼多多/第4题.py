def gcd(a,b):
    if a%b == 0:
        return b
    else :
        return gcd(b,a%b)

def gongbeishu(a, b):
    a1 = max(a, b)
    b1 = min(a, b)
    g = gcd(a1, b1)
    return a*b/g

if __name__ == '__main__':
    N,M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    total = 0
    arr.sort()
    last_dict = []
    for i in range(M):
        c = N//arr[i]
        dict1 = []
        for j in range(i):
            iou = gongbeishu(arr[i], arr[j])
            count = N // iou
            dict1.append([iou, count, 2])
            c = c - count
        n = 2
        flag = 1
        for iou, count, num in last_dict:
            if num != n:
                flag = -flag
                n = num
            new_iou = gongbeishu(iou, arr[i])
            count = N // new_iou
            dict1.append([new_iou, count, num + 1])
            c = c + flag * count
        last_dict = last_dict + dict1
        last_dict.sort(key=lambda x: x[2])
        # print(last_dict)
        total += c
    print(total)

