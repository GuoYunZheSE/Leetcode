# @Date    : 20:38 04/01/2021
# @Author  : ClassicalPi
# @FileName: 112.py
# @Software: PyCharm
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.valid=False
    def DFS(self,root:TreeNode,sum:int,targetSum:int):
        if not (root.right or root.left):
            if sum+root.val==targetSum:
                self.valid=True
        if root.left:
            self.DFS(root.left,sum+root.val,targetSum)
        if root.right:
            self.DFS(root.right,sum+root.val,targetSum)
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        self.DFS(root,0,targetSum)
        return self.valid