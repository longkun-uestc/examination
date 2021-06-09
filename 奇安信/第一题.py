def jumpFloor(number):
    count = [0, 1, 2]
    if number == 0:
        return 0
    if number == 1:
        return 1
    if number == 2:
        return 2
    for i in range(3, number + 1):
        count.append(count[i - 1] + count[i - 2])
    return count[number]
if __name__ == '__main__':
    n = int(input())
    if 0 <=n<=36:
        res = jumpFloor(n)
        print(res)
    else:
        print(0)