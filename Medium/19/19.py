# @Date    : 01:07 08/10/2020
# @Author  : ClassicalPi
# @FileName: 19.py
# @Software: PyCharm

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        Begin=head
        length=0
        while head:
            length+=1
            head=head.next
        n=length-n
        head=Begin
        if n==0:
            return head.next
        cur_node = head
        if head.next:
            next_node=head.next
        else:
            return None
        # 0->1->2->3->4 3
        while n>1:
            print("n:{} cur_node:{} next_node:{}".format(n,cur_node.val,next_node.val))
            cur_node=next_node
            next_node=cur_node.next
            n-=1
        cur_node.next=next_node.next
        return Begin

