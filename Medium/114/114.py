# @Date    : 16:44 08/28/2021
# @Author  : ClassicalPi
# @FileName: 114.py
# @Software: PyCharm
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.prev = None
    def flatten(self, root:TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return

        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
        return root