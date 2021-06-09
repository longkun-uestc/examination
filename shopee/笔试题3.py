class Node:
    def __init__(self, val):
        self.val = val
        self.path = []

def min_dis(mat_01, mat, start, end, k):
    stack = []
    start_node = Node(start)
    stack.append(start_node)
    all_path = []
    while stack:
        now = stack.pop()
        arrive_list = mat_01[now.val]
        for city, x in enumerate(arrive_list):
            if x == 0:
                continue
            if x == 1 and city != end and len(now.path) == k:
                continue
            if x == 1 and city == end and len(now.path) <= k:
                path = now.path + [now.val, city]
                all_path.append(path)
                continue
            if x == 1 and city != end and len(now.path) < k:
                node = Node(city)
                node.path = now.path + [now.val]
                stack.append(node)
    all_cost = []
    for path in all_path:
        cost = 0
        for i in range(len(path)-1):
            cost += mat[(min(path[i], path[i+1]), max(path[i], path[i+1]))]
        all_cost.append(cost)
    print(min(all_cost))

if __name__ == '__main__':
    n = int(input())
    data = input()
    tmp = data.split(" ")
    mat = {}
    mat_01 = [[0 for i in range(n)] for j in range(n)]
    for item in tmp:
        x = list(map(int, item.split(",")))
        s, e, c = x
        mat[(min(s, e), max(s, e))] = c
        mat_01[x[0]][x[1]] = 1
    start, end, k = map(int, input().split(' '))
    # print(n)
    # print(mat)
    # print(start, end, k)
    min_dis(mat_01, mat, start, end, k)

