# @Date    : 20:24 03/23/2021
# @Author  : ClassicalPi
# @FileName: 111.py
# @Software: PyCharm
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.depth=0
    def DFS(self,root:TreeNode,d:int):
        if not root.right and not root.left:
            self.depth=max(self.depth,d)
        if root.left:
            self.DFS(root.left,d+1)
        if root.right:
            self.DFS(root.right,d+1)
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.DFS(root,1)
        return self.depth