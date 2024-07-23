#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def __init__(self):
        self.result = []
        self.track = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack(n, k, 1)
        return self.result
    
    def backtrack(self, n: int, k: int, start: int) -> None:
        if len(self.track) == k:
            self.result.append(self.track.copy())
            return
        
        for i in range(start, n + 1):
            self.track.append(i)
            self.backtrack(n, k, i + 1)
            self.track.pop()

# @lc code=end

