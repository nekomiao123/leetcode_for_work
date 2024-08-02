#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if root is None:
    #         return None
        
    #     left = self.invertTree(root.left)
    #     right = self.invertTree(root.right)

    #     root.left = right
    #     root.right = left

    #     return root
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root
    
    def traverse(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        self.traverse(root.left)
        self.traverse(root.right)


# @lc code=end

