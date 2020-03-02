# @Date    : 02:22 02/29/2020
# @Author  : ClassicalPi
# @FileName: 1026.py
# @Software: PyCharm

# Definition for a binary tree node.
from Util.Tree import TreeNode

class Solution:
    def __init__(self):
        self.res=0
    def DFS(self,trace:[],root:TreeNode):
        if root.left:
            self.DFS([root.val]+trace,root.left)
        else:
            trace+=[root.val]
            self.res=max(self.res,self.find_max(trace))
        if root.right:
            self.DFS([root.val]+trace,root.right)
        else:
            trace+=[root.val]
            self.res=max(self.res,self.find_max(trace))

    def find_max(self,trace:[]):
        maximum=0
        for i in trace:
            maximum=max([abs(a-i) for a in trace])
        return maximum

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.DFS([],root)
        return self.res

if __name__ == '__main__':
    # root=TreeNode(8,TreeNode(3,TreeNode(1,None,None),TreeNode(6,TreeNode(4,None,None),TreeNode(7,None,None))),TreeNode(10,None,TreeNode(14,TreeNode(13,None,None),None)))
    # root=TreeNode(1,None,TreeNode(2,None,TreeNode(0,TreeNode(3,None,None),None)))
    l=[7,5,12,11,0,2,"null",4,17,6,19,"null",16,18,"null","null","null","null",9,14,10,"null","null","null","null","null","null","null","null",3,1,"null","null",8,"null",13,"null","null",15]
    root=TreeNode.listToTree(l)
    s=Solution()
    print(s.maxAncestorDiff(root))