# @Date    : 00:22 08/05/2021
# @Author  : ClassicalPi
# @FileName: 328.py
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        count = 1
        origin = head
        even, odd = None,None
        evenHead = None
        while head:
            if count % 2 == 0:
                if even:
                    even.next = head
                    even = even.next
                else:
                    even = head
                    evenHead = even
            else:
                if odd:
                    odd.next = head
                    odd = odd.next
                else:
                    odd = head
            head = head.next
            count += 1
        even.next = None
        odd.next = evenHead
        return origin

if __name__ == '__main__':
    S = Solution()
    N1 = ListNode(1)
    N2 = ListNode(2)
    N3 = ListNode(3)
    N4 = ListNode(4)
    N5 = ListNode(5)
    N1.next,N2.next,N3.next,N4.next = N2, N3 ,N4,N5
    a= S.oddEvenList(N1)