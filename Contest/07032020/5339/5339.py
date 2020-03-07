# @Date    : 17:01 03/07/2020
# @Author  : ClassicalPi
# @FileName: 5339.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.s=0

    def checkBST(self, root):
        self.arr = []
        self.dfs(root)
        return [self.arr == sorted(self.arr),sum(self.arr)]

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.arr.append(root.val)
        self.dfs(root.right)

    def DFS(self,root):
        if root.left:
            ans,s=self.checkBST(root.left)
            if ans:
                self.s=max(self.s,s)
            self.DFS(root.left)
        if root.right:
            ans,s=self.checkBST(root.right)
            if ans:
                self.s=max(self.s,s)
            self.DFS(root.right)

    def maxSumBST(self, root: TreeNode) -> int:
        ans, s = self.checkBST(root)
        if ans:
            self.s = max(self.s, s)
        self.DFS(root)
        return self.s
