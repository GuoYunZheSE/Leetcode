# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        Onestep=head
        Twostep=head
        while Twostep.next and Twostep.next.next:
            Onestep=Onestep.next
            Twostep=Twostep.next.next
            if Onestep==Twostep:return True
        return False