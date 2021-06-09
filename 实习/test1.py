# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         for v in values:
#             ans += v
#     print(ans)
dic = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6}
a_dic = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g"}


def to_number(s):
    num = 0
    b = 0
    for a in s[::-1]:
        num += (ord(a) - ord("a")) * (5 ** b)
        b += 1
    return num


def change(s):
    num = to_number(s)
    array = []
    while num > 0:
        array.append(a_dic[num % 7])
        num = num // 7
    result = ""
    for a in array[::-1]:
        result += a
    return result


if __name__ == '__main__':
    import sys
    for line in sys.stdin:
        s = line.strip()
        b = change(s)
        print(b)
