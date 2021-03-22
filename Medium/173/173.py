# @Date    : 16:46 03/22/2021
# @Author  : ClassicalPi
# @FileName: 173.py
# @Software: PyCharm
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.path=[]
        self.inorder(self.path,root)
        self.index=-1

    def inorder(self, res: [], root: TreeNode):
        if root.left:
            self.inorder(res, root.left)
        res.append(root.val)
        if root.right:
            self.inorder(res, root.right)

    def next(self) -> int:
        self.index +=1
        return self.path[self.index]

    def hasNext(self) -> bool:
        return self.index < len(self.path)