#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right, up, down = 0, n-1, 0, n-1
        matrix = [[0]*n for _ in range(n)]
        num = 1
        while (left <= right) and (up <= down):
            # from left to right
            for i in range(left, right+1):
                matrix[up][i] = num
                num += 1
            up += 1
            # from up to down
            for i in range(up, down+1):
                matrix[i][right] = num
                num += 1
            right -= 1
            # from left to right
            for i in range(right, left-1, -1):
                matrix[down][i] = num
                num += 1
            down -= 1
            # from down to up
            for i in range(down, up-1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
        return matrix


# @lc code=end

