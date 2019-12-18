class Solution:
    def multiply(self, A):
        left_to_right = [-1]*len(A)
        right_to_left = [-1]*len(A)
        left_to_right[0] = 1
        right_to_left[-1] = 1
        for i in range(1, len(left_to_right)):
            left_to_right[i] = left_to_right[i-1] * A[i-1]
        for i in range(len(right_to_left)-2, -1, -1):
            right_to_left[i] = right_to_left[i+1] * A[i+1]
        # B = [1]*len(A)
        # for i in range(len(B)):
        #     B[i] = left_to_right[i] * right_to_left[i]
        B = [a*b for a, b in zip(left_to_right, right_to_left)]
        # print(left_to_right)
        # print(right_to_left)
        # print(B)
        return B
if __name__ == '__main__':
    s = Solution()
    s.multiply([2,3,4,5, 6])