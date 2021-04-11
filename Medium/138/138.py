# @Date    : 16:33 04/11/2021
# @Author  : ClassicalPi
# @FileName: 138.py
# @Software: PyCharm

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node_dic={}

        origin_dic={}
        origin=head

        count=0
        while origin:
            origin_dic.setdefault(origin,count)
            origin=origin.next
            count+=1
        origin_dic.setdefault(None,count)

        count=0
        while head:
            node_dic.setdefault(count,(Node(x=head.val),origin_dic[head.random]))
            head=head.next
            count+=1
        node_dic.setdefault(count,(None,-1))

        for index,val in node_dic.items():
            node,rp=val
            if node is None:
                continue
            node.next=node_dic[index+1][0]
            node.random=node_dic[rp]
        return node_dic[0][0]