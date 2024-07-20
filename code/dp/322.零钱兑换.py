#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     memo = [-888] * (amount + 1)
    #     return self.dp(coins, amount, memo)
    
    # def dp(self, coins: List[int], amount: int, memo: List[int]) -> int:
    #     if amount == 0:
    #         return 0
    #     if amount < 0:
    #         return -1 
        
    #     if memo[amount] != -888:
    #         return memo[amount]
        
    #     res = float('inf')
    #     for coin in coins:
    #         subProblem = self.dp(coins, amount - coin, memo)
    #         if subProblem == -1:
    #             continue
    #         res = min(res, subProblem + 1)

    #     memo[amount] = res if res != float('inf') else -1
    #     return memo[amount]
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if amount - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return -1 if dp[amount] == amount + 1 else dp[amount]

# @lc code=end

