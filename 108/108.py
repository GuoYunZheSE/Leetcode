# Problem:108. Convert Sorted Array to Binary Search Tree
# Class:Easy
# Data:27/02/2019


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2  # 找到中间节点
        root = TreeNode(nums[mid])  # 当前节点为根节点
        root.left = self.sortedArrayToBST(nums[:mid])  # 小于当前根节点的作为左子树
        root.right = self.sortedArrayToBST(nums[mid + 1:])  # 大于当前根节点的作为右子树
        return root

class Solution2(object):
    def sortedArrayToBST(self,nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums ==[] or nums == None:
            return None
        root = TreeNode(0)
        stack = [[0, len(nums)-1, root]]
        while(len(stack)):
            left,right, node = stack.pop()
            middle = (left + right)//2
            node.val =  nums[middle]
            if left <= middle-1:
                node.left = TreeNode(0)
                stack.append([left, middle-1, node.left])
            if right >= middle+1:
                node.right = TreeNode(0)
                stack.append([middle+1, right, node.right])
        return root

if __name__ == '__main__':
    num = [-10, -3, 0, 5, 9]
    s = Solution2
    s.sortedArrayToBST(s,nums=num)
