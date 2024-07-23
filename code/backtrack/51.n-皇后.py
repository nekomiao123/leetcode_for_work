#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def __init__(self):
        self.result = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        self.backtrack(board, 0)
        return self.result
    
    def backtrack(self, board: List[List[str]], row: int) -> None:
        if row == len(board):
            self.result.append(["".join(rowstr) for rowstr in board])
            return

        n = len(board[row])
        for column in range(n):
            if not self.isValid(board, row, column):
                continue
            
            board[row][column] = "Q"
            self.backtrack(board, row + 1)
            board[row][column] = "."
        
    def isValid(self, board: List[List[str]], row: int, column: int) -> bool:
        n = len(board)

        # check column
        for i in range(n):
            if board[i][column] == "Q":
                return False

        # check up right
        r, c = row - 1, column + 1
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1
        
        # chek up left
        r, c = row - 1, column - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        
        return True
# @lc code=end

