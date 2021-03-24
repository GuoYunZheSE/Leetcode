# @Date    : 21:05 03/24/2021
# @Author  : ClassicalPi
# @FileName: 110.py
# @Software: PyCharm
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.valid=True
    def DFS(self,root:TreeNode,depth):
        if self.valid:
            print(f"Depth:{depth} Val:{root.val}")
            if not root.left and not root.right:
                depth+=1
                return depth
            else:
                temp1,temp2=0,0
                if root.left:
                    temp1=self.DFS(root.left,depth)
                if root.right:
                    temp2=self.DFS(root.right,depth)
                self.valid=(abs(temp2-temp1)<=1)
                depth=max(temp2,temp1)+1
                print(f"Depth:{depth} Val:{root.val}")
                return depth

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.DFS(root,1)
        return self.valid