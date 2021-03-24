# @Date    : 20:55 03/24/2021
# @Author  : ClassicalPi
# @FileName: 104.py
# @Software: PyCharm
import sys
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.depth=-sys.maxsize
    def DFS(self,root:TreeNode,d:int):
        if not root.left and not root.right:
            self.depth=max(self.depth,d)
        else:
            if root.left:
                self.DFS(root.left,d+1)
            if root.right:
                self.DFS(root.right,d+1)
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.DFS(root,1)
        return self.depth