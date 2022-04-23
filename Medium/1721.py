# @Date    : 00:15 04/10/2022
# @Author  : ClassicalPi
# @FileName: 1721.py
# @Software: PyCharm
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: [ListNode], k: int) -> [ListNode]:
        res = self
        res.next = head

        list_dic = {0:res}
        length = 1
        while head:
            list_dic.setdefault(length,head)
            length += 1
            head = head.next
        list_dic.setdefault(length, None)
        reverse_k = length - k
        pre_k, after_k = list_dic[k - 1], list_dic[k + 1]
        pre_reverse_k, after_reverse_k = list_dic[reverse_k - 1], list_dic[reverse_k + 1]

        if abs(k - reverse_k) <= 1:
            if k < reverse_k:
                pre_k.next = list_dic[reverse_k]
                list_dic[reverse_k].next = list_dic[k]
                list_dic[k].next = after_reverse_k
            elif k > reverse_k:
                pre_reverse_k.next = list_dic[k]
                list_dic[k].next = list_dic[reverse_k]
                list_dic[reverse_k].next = after_k
            else:
                return list_dic[0].next
        else:

            pre_k.next = list_dic[reverse_k]
            list_dic[reverse_k].next = after_k
            pre_reverse_k.next = list_dic[k]
            list_dic[k].next = after_reverse_k

        return list_dic[0].next