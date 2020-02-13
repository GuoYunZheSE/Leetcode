# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorder(self,root:TreeNode):
        if root:
            temp=root.left
            root.left=root.right
            root.right=temp
            self.preorder(root.left)
            self.preorder(root.right)
        else:
            return
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.preorder(root)
        return root