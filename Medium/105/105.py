# @Date    : 11:25 03/25/2021
# @Author  : ClassicalPi
# @FileName: 105.py
# @Software: PyCharm
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        dic={}
        for index,val in enumerate(inorder):
            dic.setdefault(val,index)
        def helper(start:int,end:int)->TreeNode or None:
            if start>=end:
                return None
            root_val=preorder.pop(0)
            root_index=dic[root_val]
            root=TreeNode(root_val,helper(start,root_index),helper(root_index+1,end))
            return root
        return helper(0,len(inorder))



