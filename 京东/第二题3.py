class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

if __name__ == '__main__':
    m = int(input())
    ops = []
    for i in range(m):
        op = input()
        ops.append(op)
    head = Node(-1)
    for op in ops:
        if op[0] == '1':
            _, x, y = list(map(int, op.split()))
            count = 0
            now = head
            while now and count < x-1:
                now = now.next
                count += 1
            node = Node(y)
            node.next = now.next
            now.next = now
        elif op[0] == "2":
            _, x = list(map(int, op.split()))
            count = 0
            now = head
            while now and count < x-1:
                now = now.next
                count += 1
            next = now.next
            now.next = next.next
            del next
        else:
            arr = []
            now = head.next
            while now:
                arr.append(str(now.val))
            print(' '.join(arr))