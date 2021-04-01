# @Date    : 20:17 04/01/2021
# @Author  : ClassicalPi
# @FileName: 124.py
# @Software: PyCharm
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import sys
class Solution:
    def __init__(self):
        self.res=-sys.maxsize
    def DFS(self,root:TreeNode)->int:
        lv=rv=0
        if root.left:
            lv=self.DFS(root.left)
        if root.right:
            rv=self.DFS(root.right)
        self.res=max(self.res,lv+rv+root.val)
        return max(lv+root.val,rv+root.val)
    def maxPathSum(self, root: TreeNode) -> int:
        self.DFS(root)
        return self.res

