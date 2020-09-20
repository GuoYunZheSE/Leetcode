# @Date    : 20:49 09/20/2020
# @Author  : ClassicalPi
# @FileName: 21.py
# @Software: PyCharm

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        res=ListNode()

        if l1 or l2:
            if l1 and l2:
                if l1.val<l2.val:
                    res=l1
                    l1=l1.next
                else:
                    res=l2
                    l2=l2.next
            elif l1:
                res=l1
                return res
            else:
                res=l2
                return res

        head=res

        while l1 or l2:
            if l1 and l2:
                if l1.val<=l2.val:
                    res.next=l1
                    res=res.next
                    l1=l1.next
                else:
                    l1,l2=l2,l1
            else:
                if l1:
                    res.next=l1
                    return head
                elif l2:
                    res.next=l2
                    return head
                else:
                    return head