# @Date    : 17:24 04/26/2022
# @Author  : ClassicalPi
# @FileName: 143.py
# @Software: PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: [ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node_map = {}
        dummy_head, dummy_head.next = ListNode(), head
        index = 0
        while head:
            node_map.setdefault(index, head)
            index, head = index + 1, head.next
        index -= 1
        prev = dummy_head
        for i in range(0,index // 2 + 1):
            prev.next, prev.next.next = node_map[i], node_map[index - i]
            prev = node_map[index - i]
        prev.next = None
        return dummy_head.next
if __name__ == '__main__':
    N1,N2,N3,N4,N5 = ListNode(1),ListNode(2),ListNode(3),ListNode(4),ListNode(5)
    N1.next,N2.next,N3.next,N4.next = N2, N3 ,N4, N5
    S= Solution()
    print(S.reorderList(N1))