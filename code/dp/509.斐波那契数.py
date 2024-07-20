#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    # def fib(self, n: int) -> int:
    #     memo = [0] * (n + 1)
    #     return self.dp(memo, n)

    # def dp(self, memo: List[int], n: int) -> int:
    #     if n in {0, 1}:
    #         return n
    #     if memo[n] != 0:
    #         return memo[n]
    #     memo[n] = self.dp(memo, n-1) + self.dp(memo, n-2)
    #     return memo[n]

    def fib(self, n: int) -> int:
        if n in {0, 1}:
            return n
        dp_i_2 = 0
        dp_i_1 = 1
        for _ in range(2, n + 1):
            dp_i = dp_i_1 + dp_i_2
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
        return dp_i

# @lc code=end

