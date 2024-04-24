#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p = head
        p1 = dummy1
        p2 = dummy2

        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            
            # 1.cut down the link between the orinal list to prevent the cycle.
            # tmp = p.next
            # p.next = None
            # p = tmp
            # 2.making the p2 -> None
            p = p.next
        p2.next = None 
        
        p1.next = dummy2.next
        return dummy1.next

        
# @lc code=end

