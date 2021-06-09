from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if not coins:
            return 0
        self.dict1 = {}
        def dfs(amount, coins, idx):
            if amount < 0:
                return 0
            if amount == 0:
                return 1
            if (amount, idx) in self.dict1:
                return self.dict1[(amount, idx)]
            total = 0
            for i in range(idx, len(coins)):
                if coins[i] <= amount:
                    total += dfs(amount-coins[i], coins, i)
            self.dict1[(amount, idx)] = total
            return total
        dfs(amount, coins, 0)
        print(self.dict1)
        print(self.dict1[(amount, 0)])
        return self.dict1[(amount, 0)]




if __name__ == '__main__':
    s = Solution()
    s.change(500, [1,2,5])


