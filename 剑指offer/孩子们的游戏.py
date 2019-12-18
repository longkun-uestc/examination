class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 使用两个记号数组记录上下文。这样方便查找下一个
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1
        all = [1] * n
        next = [i for i in range(1, n)]
        next.append(0)
        last = [i for i in range(n-1)]
        last.insert(0, n-1)
        num = n
        now = 0
        while num > 1:
            r = 0
            while r < m:
                if all[now] != 0:
                    if r != m-1:
                        now = next[now]
                    r += 1
                else:
                    now = next[now]
                # if all[now] != 0:
                #     if r != m - 1:
                #         now = (now + 1) % n
                #     r += 1
                # else:
                #     now = (now + 1) % n
            all[now] = 0
            flag = next[now]
            last[next[now]] = last[now]
            next[last[now]] = next[now]
            next[now] = -1
            last[now] = -1
            now = flag
            num -= 1
        print(all.index(1))
        return all.index(1)

    # 不用记号数组记录上下文的写法。这样搜索下一个还在圈内的人时容易超时。
    def LastRemaining_Solution1(self, n, m):
        if n < 1 or m < 1:
            return -1
        all = [1] * n
        num = n
        now = 0
        while num > 1:
            r = 0
            while r < m:
                if all[now] != 0:
                    if r != m - 1:
                        now = (now + 1) % n
                    r += 1
                else:
                    now = (now + 1) % n
            all[now] = 0
            # print(num, all)
            num -= 1
            now = (now + 1) % n
            while all[now] != 1:
                now = (now + 1) % n
        print(all.index(1))
        return all.index(1)

    # 双向循环链表的写法,最简洁
    def LastRemaining_Solution2(self, n, m):
        if n < 1 or m < 1:
            return -1
        # if n == 1:
        #     return 0
        head = Node(0)
        now = head
        for i in range(1, n):
            new_node = Node(i)
            now.right = new_node
            new_node.left = now
            now = new_node
        now.right = head
        head.left = now
        now = head
        residue = n
        while residue > 1:
            for r in range(0, m-1):
                now = now.right
            now.left.right = now.right
            now.right.left = now.left
            a = now
            now = now.right
            del a
            residue -= 1
        return now.val





if __name__ == '__main__':
    s = Solution()
    s.LastRemaining_Solution2(100, 13)
