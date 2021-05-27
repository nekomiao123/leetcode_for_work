#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
# 使用快慢两个指针，快指针自己一直走着，慢指针遇到特殊情况会停下来，
# 但是快指针还是一直赋值给慢指针，这样就跳过了相同的值
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, size = 0, len(nums)
        for fast in range(size):
            if val != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
        return slow
# @lc code=end

