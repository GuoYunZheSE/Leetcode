# @Date    : 15:49 03/22/2021
# @Author  : ClassicalPi
# @FileName: 145.py
# @Software: PyCharm
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorder(self,root:TreeNode,path:list):
        if root.left:
            self.postorder(root.left,path)
        if root.right:
            self.postorder(root.right,path)
        path.append(root.val)
    def postorderTraversal(self, root: TreeNode) -> [int]:
        if not root:return []
        res=[]
        self.postorder(root,res)
        return res