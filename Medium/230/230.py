# @Date    : 18:00 03/22/2021
# @Author  : ClassicalPi
# @FileName: 230.py
# @Software: PyCharm
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
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ordered=[]
        self.inorder(ordered,root)
        return ordered[k-1]
