from typing import List


class Solution:
    def findMaxLength1(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        max_len = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                dp[i] = dp[i-2] + 2 if i-2 >= 0 else 2
            else:
                if i-dp[i-1]-1 >= 0 and nums[i-dp[i-1]-1] != nums[i]:
                    dp[i] = dp[i-1]+2+dp[i-dp[i-1]-2] if i-dp[i-1]-2 >= 0 else dp[i-1]+2
                else:
                    dp[i] = 0
            max_len = max(max_len, dp[i])
        print(dp)
        return max_len

    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        cnt = 0
        cnt_dict = {}
        cnt_dict[cnt] = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt -= 1
            if cnt in cnt_dict:
                prefix = cnt_dict[cnt]
                max_len = max(max_len, i-prefix)
            else:
                cnt_dict[cnt] = i
        return max_len

if __name__ == '__main__':
    x = [0,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,1,1,0,0,0]
    # x = [0,1,1,0,1,1,1,0]
    x = [1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,0,0,1,0,1,1]
    s = Solution()
    r = s.findMaxLength1(x)
    print(x)
    print(r)
