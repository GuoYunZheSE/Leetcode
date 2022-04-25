# @Date    : 10:39 04/24/2022
# @Author  : ClassicalPi
# @FileName: 61.py
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 0 1 2 3 4
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        dummy_head, dummy_head.next = ListNode(), head
        length = 1
        while head.next:
            length += 1
            head = head.next
        if k == 0 or k % length == 0:
            return dummy_head.next
        tail = head

        left = length - k % length - 1
        pivot = dummy_head.next
        while left > 0:
            left -= 1
            pivot = pivot.next
        new_head, pivot.next = pivot.next, None
        tail.next = dummy_head.next
        return new_head

if __name__ == '__main__':
    # N5,N4,N3,N2,N1 = ListNode(5),ListNode(4),ListNode(3),ListNode(2),ListNode(1)
    # N1.next,N2.next,N3.next,N4.next = N2, N3, N4, N5
    N1,N2,N3 = ListNode(0),ListNode(1),ListNode(2)
    N1.next, N2.next = N2, N3
    S = Solution()
    print(S.rotateRight(N1,0))