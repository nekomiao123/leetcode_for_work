#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.result = []
        self.track = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backtrack(nums, 0)
        return self.result

    def backtrack(self, nums: List[int], start: int) -> None:
        self.result.append(self.track.copy())

        for i in range(start, len(nums)):
            if i > start and nums[i-1] == nums[i]:
                continue
            self.track.append(nums[i])
            self.backtrack(nums, i + 1)
            self.track.pop()

        
# @lc code=end

