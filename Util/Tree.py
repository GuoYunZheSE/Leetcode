# @Date    : 21:58 02/29/2020
# @Author  : ClassicalPi
# @FileName: Tree.py
# @Software: PyCharm
import typing
class TreeNode:
    def __init__(self, *args):
        if len(args)==1:
            self.val = args[0]
            self.left = None
            self.right = None
        if len(args)==3:
            self.val,self.left,self.right=args
    @staticmethod
    def listToTree(l:typing.List[int or str]):
        if not l:
            return TreeNode(None,None,None)
        nodes=[]
        for i in l:
            if i!="null":
                nodes.append(TreeNode(i))
            else:
                nodes.append(None)
        for i in range(0,len(nodes)):
            if nodes[i] and i<(len(nodes)//2):
                nodes[i].left=nodes[(i)*2+1]
                nodes[i].right=nodes[(i)*2+2]
        return nodes[0]


# class Solution(object):
#     def maxAncestorDiff(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not root: return 0
#         return self.helper(root, root.val, root.val)
#
#     def helper(self, node, high, low):
#         if not node:
#             return high - low
#         high = max(high, node.val)
#         low = min(low, node.val)
#         return max(self.helper(node.left, high, low), self.helper(node.right, high, low))