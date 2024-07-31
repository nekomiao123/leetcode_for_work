#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.result = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.result
    
    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.result = max(self.result, left + right)
        return max(left, right) + 1
    
# @lc code=end

