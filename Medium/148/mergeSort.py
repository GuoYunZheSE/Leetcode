# @Date    : 16:19 03/11/2021
# @Author  : ClassicalPi
# @FileName: mergeSort.py
# @Software: PyCharm
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def find_middle(Begin:ListNode)->ListNode:
    fast=Begin
    mid_prev=None
    while fast!=None and fast.next!=None:
        fast=fast.next
        fast=fast.next
        if mid_prev == None:
            mid_prev = Begin
        else:
            mid_prev = mid_prev.next
    mid = mid_prev.next
    mid_prev.next=None
    return mid

def merge(n1:ListNode,n2:ListNode)->ListNode:
    head=ListNode()
    tail=head
    while n1:
        if n2:
            if n1.val<=n2.val:
                tail.next=n1
                tail=tail.next
                n1=n1.next
            else:
                tail.next=n2
                tail = tail.next
                n2=n2.next
        else:
            tail.next=n1
            break
    if n2:
        tail.next=n2
    return head.next


def merge_sort_linked_list(Begin:ListNode)->ListNode or None:
    if Begin is None or Begin.next is None:
        return Begin
    middle=find_middle(Begin)
    l = merge_sort_linked_list(Begin)
    r =merge_sort_linked_list(middle)
    return merge(l,r)

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return merge_sort_linked_list(head)

if __name__ == '__main__':
    S=Solution()
    n1=ListNode(val=4)
    n2 = ListNode(val=2)
    n3 = ListNode(val=1)
    n4 = ListNode(val=3)
    n3.next=n4
    n2.next=n3
    n1.next=n2
    res=S.sortList(n1)