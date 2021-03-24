# @Date    : 20:53 03/23/2021
# @Author  : ClassicalPi
# @FileName: 429.py
# @Software: PyCharm
import collections


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.dict=collections.defaultdict(list)
    def DFS(self,root:Node,depth:int):
        self.dict[depth].append(root.val)
        for child in root.children:
            if child:
                self.DFS(child,depth+1)
    def levelOrder(self, root: Node) -> [[int]]:
        if not root:
            return []
        res=[]
        self.DFS(root,0)
        for i in range(max(list(self.dict.keys()))+1):
            res.append(self.dict[i])
        return res
