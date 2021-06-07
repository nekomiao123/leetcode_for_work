#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._dummyHead = Node(0)
        self._count = 0

    def get(self, index: int):
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        """
        if 0 <= index < self._count:
            node = self._dummyHead
            for _ in range(index + 1):
                node = node.next
            return node.val
        else:
            return -1

    def addAtHead(self, val: int):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion,
        the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int):
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self._count, val)

    def addAtIndex(self, index: int, val: int):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list,
        the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index < 0:
            index = 0
        elif index > self._count:
            return

        self._count += 1

        add_node = Node(val)
        prev_node = None
        cur_node = self._dummyHead 
        for _ in range(index  + 1):
            prev_node = cur_node
            cur_node = cur_node.next
        else:
            prev_node.next = add_node
            add_node.next = cur_node


    def deleteAtIndex(self, index: int):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index < self._count:
            self._count -= 1
            prev_node = None
            cur_node = self._dummyHead
            for _ in range(index  + 1):
                prev_node = cur_node
                cur_node = cur_node.next
            else:
                prev_node.next = cur_node.next
                cur_node.next = None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end
