# @Date    : 17:18 04/26/2022
# @Author  : ClassicalPi
# @FileName: 203.py
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: [ListNode], val: int) -> [ListNode]:
        dummy_head, dummy_head.next = ListNode(), head
        prev = dummy_head
        while head:
            if head.val == val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return dummy_head.next
