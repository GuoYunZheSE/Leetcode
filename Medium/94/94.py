# @Date    : 11:43 03/22/2021
# @Author  : ClassicalPi
# @FileName: 94.py
# @Software: PyCharm
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorder(self,root:TreeNode,path:[]):
        if not root.right and not root.left:
            path.append(root.val)
            return
        if root.left:
            self.inorder(root.left,path)
        path.append(root.val)
        if root.right:
            self.inorder(root.right,path)
    def inorderTraversal(self, root: TreeNode) -> [int]:
        if not root:
            return []
        res=[]
        self.inorder(root,res)
        return res