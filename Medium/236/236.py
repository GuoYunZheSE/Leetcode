# @Date    : 21:26 07/08/2021
# @Author  : ClassicalPi
# @FileName: 236.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.childrenMap = {}
        self.found = False
        self.res = TreeNode(-10086)
    def BottumUpDFS(self,root:'TreeNode',p: int, q: int):
        if not self.found:
            childrenLeft = []
            childrenRight = []
            if root.left:
                childrenLeft = self.BottumUpDFS(root.left,p,q)
            if root.right:
                childrenRight = self.BottumUpDFS(root.right,p,q)
            allChildren = childrenLeft+childrenRight+[root.val]
            if p in allChildren and q in allChildren and self.res.val==-10086:
                self.found = True
                self.res = root
                return []
            return allChildren
        else:
            return []

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.BottumUpDFS(root,p.val,q.val)
        return self.res