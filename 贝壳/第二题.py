import math
n, m = list(map(int, input().split()))
ai = list(map(int, input().split()))
pi = list(map(int, input().split()))
def min_price(a, b, ans):
    if not a:
        return ans
    leastP = min(b)
    leastP_index = b.index(leastP)
    new_a1 = a[:leastP_index]
    new_a2 = a[leastP_index:]
    new_b = b[:leastP_index]
    pro_num = sum(new_a2)
    ans += math.ceil(pro_num/m)*leastP+min_price(new_a1, new_b, ans)
    return ans

print(min_price(ai, pi, 0))