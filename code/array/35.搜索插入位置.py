#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
# 因为使用的左闭右闭区间，找不到值的话最后left和right一定会相等（而且这个位置就是应该插入的位置）
# 相等之后的下一次循环，right会被减一,所以这个时候返回的left的值就是应该插入的位置
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if target < nums[middle]:
                right = middle - 1 
            elif target > nums[middle]:
                left = middle + 1
            else:
                return middle
        return left 

# @lc code=end

