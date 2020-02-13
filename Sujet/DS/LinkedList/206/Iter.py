# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre=None
        if not head:
            return head
        while head.next:

            temp=head.next
            head.next=pre

            pre=head
            head=temp
        head.next=pre
        return head