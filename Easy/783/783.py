# @Date    : 18:05 03/22/2021
# @Author  : ClassicalPi
# @FileName: 783.py
# @Software: PyCharm
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorder(self, res: [], root: TreeNode):
        if root.left:
            self.inorder(res, root.left)
        res.append(root.val)
        if root.right:
            self.inorder(res, root.right)
    def minDiffInBST(self, root: TreeNode) -> int:
        path=[]
        self.inorder(path,root)
        res=[path[i+1]-path[i] for i in range(0,len(path)-1)]
        return min(res)
