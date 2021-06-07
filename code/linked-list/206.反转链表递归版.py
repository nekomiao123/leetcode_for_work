#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self, pre, cur):
        if cur == None:
            return pre
        tmp = cur.next
        cur.next = pre
        return self.reverse(cur, tmp)

    def reverseList(self, head: ListNode):
        return self.reverse(None, head)
        

# @lc code=end

