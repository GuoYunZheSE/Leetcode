# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x,Left,Right):
        self.val = x
        self.left = Left
        self.right = Right

class Solution:

    def updateDic(self,A:int,length:int):

        if self.res.__contains__(length):
            temp=self.res.get(length)
            temp.append(A)
            self.res.update({length:temp})
        else:
            self.res.setdefault(length,[A])

    def iterTree(self,node:TreeNode,currentDepth:int):
        if node.left is not None:
            self.iterTree(node.left,currentDepth+1)

        self.updateDic(node.val,currentDepth)

        if node.right is not None:
            self.iterTree(node.right,currentDepth+1)

    def rightSideView(self, root: TreeNode) -> [int]:
        if root is None:
            return []
        self.res={0:[root.val]}
        currentDepth=0
        self.iterTree(root,currentDepth)
        Depth=max(list(self.res.keys()))
        return [self.res.get(i)[-1] for i in range(0,Depth+1)]

if __name__ == '__main__':
    root=TreeNode(1,TreeNode(2,None,TreeNode(5,None,None)),TreeNode(3,None,TreeNode(4,TreeNode(7,None,None),TreeNode(8,None,None))))
    # root=TreeNode(1,TreeNode(2,TreeNode(4,None,None),None),TreeNode(3,None,None))
    S=Solution()
    print(S.rightSideView(root))
