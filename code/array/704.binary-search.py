#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if target < nums[middle]:
                right = middle -1 
            elif target > nums[middle]:
                left = middle +1
            else:
                return middle
        return -1

# @lc code=end
