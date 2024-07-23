#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.result = []
        self.track = []
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        nums.sort()
        self.backtrack(nums, used)
        return self.result

    def backtrack(self, nums: List[int], used: List[bool]) -> None:
        if len(self.track) == len(nums):
            self.result.append(self.track.copy())
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i-1] == nums[i] and not used[i-1]:
                continue
            self.track.append(nums[i])
            used[i] = True
            self.backtrack(nums, used)
            self.track.pop()
            used[i] = False
            
# @lc code=end

