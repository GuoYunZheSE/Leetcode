# @Date    : 11:55 04/09/2022
# @Author  : ClassicalPi
# @FileName: 24.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: [ListNode]) -> [ListNode]:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next

if __name__ == '__main__':
    N4 = ListNode(4)
    N3 = ListNode(3, N4)
    N2 = ListNode(2, N3)
    N1 = ListNode(1, N2)
    S = Solution()
    a = S.swapPairs(N1)