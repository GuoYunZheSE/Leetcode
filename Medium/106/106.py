# @Date    : 17:06 03/25/2021
# @Author  : ClassicalPi
# @FileName: 106.py
# @Software: PyCharm
# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: [int], postorder: [int]) -> TreeNode:
        index_map={val:index for index,val in enumerate(inorder)}
        postorder=collections.deque(postorder[::-1])
        def helper(start:int,end:int):
            if start>=end:
                return None
            root_val=postorder.popleft()
            root_index=index_map[root_val]
            right=helper(root_index+1,end)
            left=helper(start,root_index)
            root_node=TreeNode(root_val,left,right)
            return root_node
        return helper(0,len(inorder))

if __name__ == '__main__':
    S=Solution()
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    print(S.buildTree(inorder,postorder))