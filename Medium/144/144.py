# @Date    : 15:45 03/22/2021
# @Author  : ClassicalPi
# @FileName: 144.py
# @Software: PyCharm
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorder(self,root:TreeNode,path:[int]):
        path.append(root.val)
        if root.left:
            self.preorder(root.left,path)
        if root.right:
            self.preorder(root.right,path)
    def preorderTraversal(self, root: TreeNode) -> [int]:
        res=[]
        if not root:
            return []
        self.preorder(root,res)
        return res
