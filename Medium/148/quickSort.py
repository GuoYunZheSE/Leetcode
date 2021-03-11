# @Date    : 15:28 03/11/2021
# @Author  : ClassicalPi
# @FileName: quickSort.py
# @Software: PyCharm
# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap(n1:ListNode,n2:ListNode):
    n1.val,n2.val=n2.val,n1.val

def partition(Begin:ListNode,End:ListNode or None)->ListNode:
    pivot=Begin.val
    i=Begin
    j=Begin.next
    while j != End:
        if j.val<pivot:
            i=i.next
            swap(i,j)
        j=j.next
    swap(i,Begin)
    return i

def quick_sort_linked_list(Begin:ListNode,End:ListNode or None):
    if Begin!=End:
        pivot=partition(Begin,End)
        quick_sort_linked_list(Begin,pivot)
        quick_sort_linked_list(pivot.next,End)

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        quick_sort_linked_list(head,None)
        return head