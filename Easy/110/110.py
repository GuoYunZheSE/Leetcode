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
            if not root.left and not root.right:
                return 1
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
        else:
            print(f"Depth:{depth} Val:{root.val} -1")
            return -1

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.DFS(root,1)
        return self.valid

if __name__ == '__main__':
    S=Solution()
    N1=TreeNode(1)
    N2 = TreeNode(2)
    N3 = TreeNode(2)
    N4 = TreeNode(3)
    N5 = TreeNode(3)
    N6 = TreeNode(4)
    N7 = TreeNode(4)
    N1.left=N2
    N1.right=N3
    N2.left=N4
    N3.right=N5
    N4.left=N6
    N5.right=N7
    print(S.isBalanced(N1))