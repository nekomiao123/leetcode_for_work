#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
# 还是使用双指针法
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        slow, size = 0, len(nums)
        for fast in range(1,size):
            if (nums[slow] != nums[fast]):
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1

# @lc code=end

