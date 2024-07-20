#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = dict()
        def dp(i, j):
            # base case
            if i == -1: 
                return j + 1
            if j == -1:
                return i + 1
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i - 1, j - 1) # nothing to do
            else:
                memo[(i, j)] =  min(
                    dp(i, j - 1) + 1, # add one 
                    dp(i - 1, j) + 1, # delete one 
                    dp(i - 1, j - 1) + 1 # replace one 
                )
            return memo[(i, j)]

        return dp(len(word1) - 1, len(word2) - 1)
# @lc code=end

