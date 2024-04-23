#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 初始化
        head = ListNode(0)
        cur = head
        carry = 0
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, val = divmod(val1 + val2 + carry, 10)
            cur.next = ListNode(val)
            cur = cur.next
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return head.next
# @lc code=end

