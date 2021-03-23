# @Date    : 20:32 03/23/2021
# @Author  : ClassicalPi
# @FileName: 637.py
# @Software: PyCharm
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def DFS(self,root:TreeNode,depth:int):
        self.dict[depth].append(root.val)
        if root.left:
            self.DFS(root.left,depth+1)
        if root.right:
            self.DFS(root.right,depth+1)
    def __init__(self):
        self.dict=collections.defaultdict(list)
    def averageOfLevels(self, root: TreeNode) -> [float]:
        res=[]
        self.DFS(root,0)
        for i in range(max(list(self.dict.keys()))+1):
            res.append(sum(self.dict[i])/len(self.dict[i]))
        return res