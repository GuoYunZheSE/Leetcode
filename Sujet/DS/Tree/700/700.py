# @Date    : 20:02 05/23/2020
# @Author  : ClassicalPi
# @FileName: 700.py
# @Software: PyCharm

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def DFS(self,cur:TreeNode,val:int):
        if cur.left:
            self.DFS(cur.left,val)
        if cur.val==val:
            print(cur.val)
            return cur
        if cur.right:
            self.DFS(cur.right,val)
        return None
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.DFS(root,val)