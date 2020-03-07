# @Date    : 15:50 03/07/2020
# @Author  : ClassicalPi
# @FileName: 5338.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, x,y,z):
        self.val = x
        self.left = y
        self.right = z

class Solution:
    def __init__(self):
        self.depth=0
    def DFS(self,root:TreeNode,direction:[int],d:int):
        for i in direction:
            if i==0:
                if root.right:
                    self.DFS(root.right,[1],d+1)
                else:
                    self.depth=max(self.depth,d)
            else:
                if root.left:
                    self.DFS(root.left,[0],d+1)
                else:
                    self.depth=max(self.depth,d)
    def check(self,root):
        if root.left:
            self.DFS(root.left, [0,1], 0)
            self.check(root.left)
        if root.right:
            self.DFS(root.right, [0, 1], 0)
            self.check(root.right)
    def longestZigZag(self, root: TreeNode) -> int:
        self.DFS(root,[0,1],0)
        self.check(root)
        return self.depth
