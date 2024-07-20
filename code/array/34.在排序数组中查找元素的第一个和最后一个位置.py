#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from typing import List
# @lc code=start
class Solution:
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     left, right = 0, len(nums) - 1
    #     final_left = -1
    #     final_right = -1
    #     while left <= right:
    #         mid = left + (right - left) // 2 
    #         if nums[mid] == target:
    #             final_left = mid
    #             final_right = mid
    #             break
    #         elif nums[mid] > target:
    #             right = mid - 1
    #         elif nums[mid] < target:
    #             left = mid + 1

    #     if final_left != -1:
    #         while final_left - 1 >= 0 and nums[final_left - 1] == target:
    #             final_left -= 1
    #         while final_right + 1 < len(nums) and nums[final_right + 1] == target:
    #             final_right += 1
               
    #     return [final_left, final_right] 
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirstPosition():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            if left < len(nums) and nums[left] == target:
                return left
            return -1

        def findLastPosition():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            if right >= 0 and nums[right] == target:
                return right
            return -1

        return [findFirstPosition(), findLastPosition()]
# @lc code=end

if __name__ == '__main__':
    nums = [5,7,7,8,8,10]
    target = 7
    test = Solution()
    find = test.searchRange(nums, target)
    print(find)
