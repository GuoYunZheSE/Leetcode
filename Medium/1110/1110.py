# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x,l,r):
        self.val = x
        self.left = l
        self.right = r

class Solution:
    def DFS(self,root:TreeNode,target:int)->[TreeNode]:
        if root.left is not None:
            if root.left.val !=target:
                self.DFS(root.left,target)
            else:
                if root.left.left is not None and root.left.left.val not in self.to_delete_set:
                    self.roots.append(root.left.left)
                if root.left.right is not None and root.left.right.val not in self.to_delete_set:
                    self.roots.append(root.left.right)
                root.left=None
                return
            # self.roots.append(a for a in [root.left,root.right] if a is not None and a.val not in self.to_delete_set)
        if root.right is not None:
            if root.right.val !=target:
                self.DFS(root.right,target)
            else:
                if root.right.left is not None and root.right.left.val not in self.to_delete_set:
                    self.roots.append(root.right.left)
                if root.right.right is not None and root.right.right.val not in self.to_delete_set:
                    self.roots.append(root.right.right)
                root.right=None
                return
    def delNodes(self, root: TreeNode, to_delete: [int]) -> [TreeNode]:
        self.to_delete_set=set(to_delete)
        self.roots = []

        if root.val in self.to_delete_set:
            if root.left is not None and root.left.val not in self.to_delete_set:
                self.roots.append(root.left)
            if root.right is not None and root.right.val not in self.to_delete_set:
                self.roots.append(root.right)
            # root = None
        else:
            self.roots.append(root)
        for each in to_delete:
            for eachroot in self.roots:
                self.DFS(eachroot,each)
        return self.roots
if __name__ == '__main__':
    root=TreeNode(1,TreeNode(2,TreeNode(4,None,None),TreeNode(5,None,None)),TreeNode(3,TreeNode(6,None,None),TreeNode(7,None,None)))
    dele=[3,5]
    S=Solution()
    ans=S.delNodes(root,dele)
    for each in ans:
        print(each.val)