# @Date    : 09:35 04/16/2021
# @Author  : ClassicalPi
# @FileName: 160.py
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
import collections
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        d=collections.defaultdict(int)
        while headA:
            d[headA]+=1
            headA=headA.next
        while headB:
            d[headB]+=1
            headB=headB.next
        for k,v in d.items():
            if v==2:
                return k
        return None