# @Date    : 19:07 03/23/2021
# @Author  : ClassicalPi
# @FileName: 120.py
# @Software: PyCharm
# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.dict=collections.defaultdict(list)
    def BFS(self,root:TreeNode,Depth:int):
        self.dict[Depth].append(root.val)
        if root.left:
            self.BFS(root.left,Depth+1)
        if root.right:
            self.BFS(root.right,Depth+1)
    def levelOrder(self, root: TreeNode) -> [[int]]:
        if not root:
            return []
        self.BFS(root,0)
        res=[]
        for i in range(max(list(self.dict.keys()))):
            res.append(self.dict[i])
        return res
