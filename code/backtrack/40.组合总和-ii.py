#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.result = []
        self.track = []
        self.trackSum = 0

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backtrack(candidates, target, 0)
        return self.result

    def backtrack(self, candidates: List[int], target: int, start: int) -> None:
        if self.trackSum == target:
            self.result.append(self.track.copy())
            return
        if self.trackSum > target:
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i-1] == candidates[i]:
                continue
            self.track.append(candidates[i])
            self.trackSum += candidates[i]
            self.backtrack(candidates, target, i + 1)
            self.track.pop()
            self.trackSum -= candidates[i]

# @lc code=end

