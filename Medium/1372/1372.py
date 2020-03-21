# @Date    : 15:50 03/07/2020
# @Author  : ClassicalPi
# @FileName: 1372.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, x,y,z):
        self.val = x
        self.left = y
        self.right = z

class Solution:
    def __init__(self):
        self.depth=0
    def DFS(self,root:TreeNode,direction:int,d:int):
        self.depth=max(d,self.depth)
        if not root:
            return
        if direction==0:
            self.DFS(root.right,1,d+1)
            self.DFS(root.left, 0, 0)
        else:
            self.DFS(root.left,0,d+1)
            self.DFS(root.right, 1, 0)
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.DFS(root.left,0,0)
        self.DFS(root.right, 1, 0)
        return self.depth
