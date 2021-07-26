# @Date    : 21:03 07/08/2021
# @Author  : ClassicalPi
# @FileName: 234.py
# @Software: PyCharm
# Definition for singly-linked list.
import collections
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        queue = collections.deque([])
        while head:
            queue.append(head.val)
            head = head.next
        for i in range(len(queue)//2):
            if queue[0] == queue [-1]:
                queue.pop()
                queue.popleft()
        return len(queue)==0 or len(queue)==1