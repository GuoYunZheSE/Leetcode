# @Date    : 21:12 04/01/2021
# @Author  : ClassicalPi
# @FileName: 687.py
# @Software: PyCharm
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res=(1001,0)
    def DFS(self,root:TreeNode)->(int,int):

        if not (root.left or root.right):
            return root.val, 1

        lf=rg=(1001,0)
        if root.left:
            lf = self.DFS(root.left)
        if root.right:
            rg = self.DFS(root.right)
        if lf[0]==rg[0]==root.val:
            if lf[1]+rg[1]>self.res[1]:
                self.res=(lf[0],lf[1]+rg[1])
            return (root.val,max(lf[1],rg[1])+1)

        if lf[0]==root.val:
            if lf[1]>self.res[1]:
                self.res=lf
            return (root.val,lf[1]+1)

        if rg[0]==root.val:
            if rg[1]>self.res[1]:
                self.res=rg
            return (root.val,rg[1]+1)

        return root.val,1

    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.DFS(root)
        return self.res[1]