# @Date    : 19:45 03/23/2021
# @Author  : ClassicalPi
# @FileName: 103.py
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
    def BFS(self,root:TreeNode,depth:int):
        self.dict[depth].append(root.val)
        if root.left:
            self.BFS(root.left,depth+1)
        if root.right:
            self.BFS(root.right,depth+1)
    def zigzagLevelOrder(self, root: TreeNode) -> [[int]]:
        if not root:
            return []
        reverse=False
        res=[]
        self.BFS(root,0)
        for i in range(max(list(self.dict.keys()))+1):
            if not reverse:
                res.append(self.dict[i])
                reverse=not reverse
            else:
                self.dict[i].reverse()
                res.append(self.dict[i])
                reverse = not reverse
        return res