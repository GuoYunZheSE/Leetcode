# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next or m==n:
            return head

        # If reverse from the very begining, we dont need pre, we make it None.
        # Else, we compute the prefore linked list and save it for the future usage.
        if m==1:
            pre=None
            reverse = head
        else:
            pre=head
            for i in range(1,m-1):
                pre = pre.next
            reverse=pre.next
        rest=reverse

        for length in range(0,n-m+1):
            if rest:
                rest=rest.next
            else:
                rest=None

        for length in range(0, n - m + 1):
            reverse2=reverse.next
            reverse.next=rest
            rest=reverse
            reverse=reverse2

        if not pre:
            return rest
        pre.next=rest
        return head


