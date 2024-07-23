#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def __init__(self):
        self.result = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        track = []
        self.backtrack(nums, track, 0)
        return self.result
    
    def backtrack(self, nums: List[int], track: List[int], start: int) -> None:
        self.result.append(track.copy())

        for i in range(start, len(nums)):
            track.append(nums[i])
            self.backtrack(nums, track, i + 1)
            track.pop()

# @lc code=end

