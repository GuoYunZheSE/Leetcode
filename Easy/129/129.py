# @Date    : 20:57 04/01/2021
# @Author  : ClassicalPi
# @FileName: 129.py
# @Software: PyCharm
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res=0
    def DFS(self,root:TreeNode,path:str):
        if not (root.left or root.right):
            self.res+=int(path+str(root.val))
        if root.left:
            self.DFS(root.left,path+str(root.val))
        if root.right:
            self.DFS(root.right,path+str(root.val))
    def sumNumbers(self, root: TreeNode) -> int:
        self.DFS(root,"")
        return self.res
