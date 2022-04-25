# @Date    : 11:17 04/24/2022
# @Author  : ClassicalPi
# @FileName: 25.py
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(head:ListNode, tail:ListNode)->(ListNode,ListNode):
            def handler(cur:ListNode, prev:ListNode or None):
                if cur != tail:
                    handler(cur.next, cur)
                cur.next = prev
            handler(head, None)
            return tail, head
        dummy_head, dummy_head.next = ListNode(0), head
        length, current_node, current_head, current_tail, pre_tail = 0, head, head, None, dummy_head
        while current_node:
            length += 1
            if length % k == 0:
                current_tail = current_node
                current_node, after = current_tail.next, current_tail.next
                reversed_head, reversed_tail = reverse(current_head, current_tail)
                pre_tail.next = reversed_head
                reversed_tail.next = after
                pre_tail = reversed_tail
                current_head = after
            else:
                current_node = current_node.next
        return dummy_head.next
if __name__ == '__main__':
    N1,N2,N3,N4,N5 = ListNode(1),ListNode(2),ListNode(3),ListNode(4),ListNode(5)
    N1.next,N2.next,N3.next,N4.next = N2,N3,N4,N5
    S = Solution()
    print(S.reverseKGroup(N1,5))