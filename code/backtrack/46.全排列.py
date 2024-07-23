#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def __init__(self):
        self.result = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        track = []
        used = [False] * len(nums)
        self.backtrack(nums, track, used)
        return self.result
    def backtrack(self, nums: List[int], track: List[int], used: List[bool]):
        if len(track) == len(nums):
            self.result.append(track.copy())
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue

            track.append(nums[i])
            used[i] = True
            self.backtrack(nums, track, used)
            track.pop()
            used[i] = False
        
# @lc code=end

