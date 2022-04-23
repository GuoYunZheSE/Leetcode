# @Date    : 13:56 04/23/2022
# @Author  : ClassicalPi
# @FileName: 86.py
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: [ListNode], x: int) -> [ListNode]:
        before, after = ListNode(0), ListNode(0)
        before_head, after_head = before, after
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        after.next = None
        before.next = after_head.next
        return before_head.next