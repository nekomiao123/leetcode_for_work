#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0
        self.depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.result

    def traverse(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return

        self.depth += 1
        if root.left is None and root.right is None:
            self.result = max(self.result, self.depth)
        self.traverse(root.left)
        self.traverse(root.right)
        self.depth -= 1
# @lc code=end

