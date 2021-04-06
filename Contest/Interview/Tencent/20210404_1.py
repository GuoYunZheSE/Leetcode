# @Date    : 19:53 04/04/2021
# @Author  : ClassicalPi
# @FileName: 20210404_1.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 你需要返回一个指针，指向root，表示删减去若干个点后，剩下的树
# @param root TreeNode类 指向二叉树的根
# @return TreeNode类
#
class Solution:
    def DFS(self,root:TreeNode):
        if not (root.left and root.right):
            if not root.right and not root.left:
                return
            else:
                root.left=None
                root.right=None
        if root.left:
            self.DFS(root.left)
        if root.right:
            self.DFS(root.right)
    def solve(self , root ):
        self.DFS(root)
        return root