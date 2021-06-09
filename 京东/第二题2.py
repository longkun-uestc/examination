class Node():
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

if __name__ == '__main__':
    m = int(input())
    ops = []
    for i in range(m):
        op = input()
        ops.append(op)
    head = Node()
    tail = Node()
    head.next = tail
    tail.pre = head
    node_dict = {}
    for op in ops:
        if op[0] == "1":
            _, x, y = list(map(int, op.split()))
            now = head
            count = 0
            while now and count < x-1:
                now = now.next
                count += 1
            node = Node(x-1, y)
            node.next = now.next
            node.pre = now
            now.next.pre = node
            now.next = node
            # node_dict[x-1] = node
        elif op[0] == "2":
            _, x = list(map(int, op.split()))
            count = 0
            now = head
            while now and count < x:
                now = now.next
                count += 1
            now.pre.next = now.next
            now.next.pre = now.pre
            del now
        else:
            arr = []
            now = head.next
            while now != tail:
                arr.append(str(now.val))
            print(' '.join(arr))



