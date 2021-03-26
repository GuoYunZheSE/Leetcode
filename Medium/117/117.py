# @Date    : 10:32 03/26/2021
# @Author  : ClassicalPi
# @FileName: 117.py
# @Software: PyCharm

import collections
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def __init__(self):
        self.dict=collections.defaultdict(list)
    def DFS(self,root:Node,depth:int):
        self.dict[depth].append(root)
        if root.left:
            self.DFS(root.left,depth+1)
        if root.right:
            self.DFS(root.right,depth+1)
    def connect(self, root: 'Node') -> 'Node':
        if not root or root==[]:
            return root
        self.DFS(root,0)
        for i in range(1,max(list(self.dict.keys()))+1):
            for index,val in enumerate(self.dict[i]):
                if index!=len(self.dict[i])-1:
                    val.next=self.dict[i][index+1]
        return root
