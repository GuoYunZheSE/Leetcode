# @Date    : 14:55 03/23/2021
# @Author  : ClassicalPi
# @FileName: 101.py
# @Software: PyCharm
# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.valid=True
    def compare(self,left:TreeNode,right:TreeNode):
        if not self.valid:
            return
        if left is None and right is None:
            return
        if left is None or right is None:
            self.valid=False
            return
        self.valid=left.val==right.val
        self.compare(left.left,right.right)
        self.compare(left.right,right.left)
    def isSymmetric(self, root: TreeNode) -> bool:
        self.compare(root.left,root.right)
        return self.valid

if __name__ == '__main__':
    Node1=TreeNode(val=1)
    Node2 = TreeNode(val=2)
    Node3 = TreeNode(val=2)
    Node4 = TreeNode(val=2)
    Node5 = TreeNode(val=2)
    Node1.right=Node3
    Node3.left=Node5
    Node1.left=Node2
    Node2.left=Node4
    S=Solution()
    print(S.isSymmetric(Node1))