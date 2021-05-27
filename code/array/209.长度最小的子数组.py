#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
# 用滑动窗口的办法解决这个问题。其实非常类似于双指针。
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float("inf")
        left = 0
        sum = 0
        for right in range(len(nums)):
            sum += nums[right]
            while(sum >= target):
                sublength = right - left + 1
                result = min(result, sublength)
                sum -= nums[left]
                left += 1
        return 0 if result==float("inf") else result

# @lc code=end

