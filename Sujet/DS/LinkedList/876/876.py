
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        trace=[]
        while head is not None:
            trace.append(head)
            head=head.next
        return trace[int(len(trace)/2)]
