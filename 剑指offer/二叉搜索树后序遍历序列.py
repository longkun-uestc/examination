# 二叉搜索树的概念
def cmp(sequence):
    if len(sequence) == 0 or len(sequence) == 1:
        return True
    now = sequence.pop()
    ids = 0
    for i in range(len(sequence)):
        if sequence[i] < now:
            ids += 1
        else:
            break
    if ids == len(sequence):
        return cmp(sequence)
    if now > min(sequence[ids:]):
        return False
    else:
        return cmp(sequence[:ids]) and cmp(sequence[ids:])


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 0:
            return False
        if cmp(sequence):
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    x = [4,8,6,12,16,14,10]
    x = [4,6,7,5]
    s.VerifySquenceOfBST(x)
