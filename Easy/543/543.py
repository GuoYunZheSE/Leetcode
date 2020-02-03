# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x,l,r):
        self.val = x
        self.left = l
        self.right = r

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1
if __name__ == '__main__':
    root=TreeNode(4,TreeNode(2,TreeNode(3,None,None),TreeNode(1,TreeNode(5,None,None),None)),None)
    s=Solution()
    print(s.diameterOfBinaryTree(root))

