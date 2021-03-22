# @Date    : 14:49 03/22/2021
# @Author  : ClassicalPi
# @FileName: 98.py
# @Software: PyCharm
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorder(self,res:[],root:TreeNode):
        if root.left:
            self.inorder(res,root.left)
        res.append(root.val)
        if root.right:
            self.inorder(res,root.right)
    def isValidBST(self, root: TreeNode) -> bool:
        res=[]
        self.inorder(res,root)
        for i in range(0,len(res)-1):
            if res[i]>=res[i+1]:
                return False
        return True
