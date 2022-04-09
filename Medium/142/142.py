# @Date    : 17:31 08/28/2021
# @Author  : ClassicalPi
# @FileName: 142.py
# @Software: PyCharm
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        res = {}
        while head:
            res[head] = res.get(head,0) + 1
            if res[head]>= 2:
                return res[head]
            head = head.next
        return ListNode(None)
if __name__ == '__main__':
    S = Solution()
    N = ListNode(1)
    print(S.detectCycle(N))