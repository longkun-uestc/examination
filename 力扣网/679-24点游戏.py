from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        target = 24
        esp = 1e-6
        ADD, MUL, SUB, DIV = 0, 1, 2, 3

        def check_24(nums):
            if not nums:
                return False
            if len(nums) == 1:
                return abs(target - nums[0]) < esp
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    new_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    for k in range(4):
                        if k < 2 and i>j:
                            continue
                        if k == ADD:
                            new_nums.append(nums[i] + nums[j])
                        elif k == MUL:
                            new_nums.append(nums[i] * nums[j])
                        elif k == SUB:
                            new_nums.append(nums[i] - nums[j])
                        else:
                            if abs(nums[j]) / esp:
                                continue
                            else:
                                new_nums.append(nums[i] / nums[j])
                        if check_24(new_nums):
                            return True
                        new_nums.pop()
            return False
        return check_24(nums)
