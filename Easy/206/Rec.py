# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def reverse(self, pre: ListNode or None, rest:ListNode):
        temp=rest.next
        rest.next = pre
        if temp:
            rest=self.reverse(rest, temp)
        return rest

    def reverseList(self, head: ListNode) -> ListNode:
        ans=None
        if not head:
            return head
        return self.reverse(ans,head)