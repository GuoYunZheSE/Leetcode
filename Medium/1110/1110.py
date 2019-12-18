# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x,l,r):
        self.val = x
        self.left = l
        self.right = r

class Solution:

    def find_roots(self, root, temp:list):
        if root.val in self.to_delete_set:
            if root.left is not None:
                self.find_roots(root.left, temp)
            if root.right is not None:
                self.find_roots(root.right, temp)
        else:
            temp.append(root)
        return temp

    def DFS(self,root:TreeNode)->[TreeNode]:
        if root.left is not None:
            if root.left.val not in self.to_delete_set:
                self.DFS(root.left)
            else:
                if root.left.left is not None:
                    self.roots+=self.find_roots(root.left.left, [])
                if root.left.right is not None:
                    self.roots+=self.find_roots(root.left.right, [])
                root.left=None
            # self.roots.append(a for a in [root.left,root.right] if a is not None and a.val not in self.to_delete_set)
        if root.right is not None:
            if root.right.val not in self.to_delete_set:
                self.DFS(root.right)
            else:
                if root.right.left is not None:
                    self.roots+=self.find_roots(root.right.left, [])
                if root.right.right is not None:
                    self.roots+=self.find_roots(root.right.right, [])
                root.right=None

    def delNodes(self, root: TreeNode, to_delete: [int]) -> [TreeNode]:
        self.roots=[]
        self.to_delete_set=set(to_delete)
        self.roots+=self.find_roots(root, [])
        for eachroot in self.roots:
            self.DFS(eachroot)
        return self.roots

if __name__ == '__main__':
    root=TreeNode(1,TreeNode(2,TreeNode(4,None,None),TreeNode(5,None,None)),TreeNode(3,TreeNode(6,None,None),TreeNode(7,None,None)))
    dele=[3,5]
    S=Solution()
    S.roots = []
    S.to_delete_set = set(dele)
    # ans=S.delNodes(root,dele)
    # for each in ans:
    #     print(each.val)
    S.roots+=[a for a in [root.left, root.right] if a is not None and a.val not in S.to_delete_set]
    print(S.roots)