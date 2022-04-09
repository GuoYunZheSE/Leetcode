# @Date    : 22:44 08/31/2021
# @Author  : ClassicalPi
# @FileName: 337.py
# @Software: PyCharm
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def DFS(root:TreeNode):
            res = [0, root.val]
            if root.left:
                temp = DFS(root.left)
                res[0] += max(temp)
                res[1] += temp[0]
            if root.right:
                temp = DFS(root.right)
                res[0] += max(temp)
                res[1] += temp[0]
            return res
        res = DFS(root)
        return max(res)