# @Date    : 12:36 06/30/2020
# @Author  : ClassicalPi
# @FileName: 2.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getLength(self,l:ListNode):
        length=1
        while l.next:
            length+=1
            l=l.next
        return length
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        Longer=l1
        Shorter=l2
        if self.getLength(l1)<self.getLength(l2):
            Longer=l2
            Shorter=l1
        Head=Longer
        for i in range(self.getLength(Shorter)):
            Longer.val+=Shorter.val
            temp=Longer
            while temp and temp.val>=10:
                if temp.next:
                    temp.next.val+=1
                else:
                    temp.next=ListNode(1,None)
                temp.val-=10
                temp=temp.next
            Longer=Longer.next
            Shorter=Shorter.next
        return Head

if __name__ == '__main__':
    L1=ListNode(2,ListNode(4,ListNode(3,None)))
    L2=ListNode(5,ListNode(6,ListNode(4,None)))
    S=Solution()
    S.addTwoNumbers(L1,L2)