class Solution:
    def searchInsert(self, nums, target) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if target < nums[middle]:
                right = middle - 1 
            elif target > nums[middle]:
                left = middle + 1
            else:
                return middle

        print("left",left)
        print("right",right)

        return left 


if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 7 
    solution = Solution()
    solution.searchInsert(nums, target)



