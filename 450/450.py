class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
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

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            if not root.left:
                return root.right

            if not root.right:
                return root.left

            minNode = root.right
            while minNode.left:
                minNode = minNode.left
            root.val = minNode.val
            root.right = self.deleteNode(root.right, minNode.val)
            return root
if __name__ == '__main__':
    S=Solution
    nums=[0]
    root=S.sortedArrayToBST(S,nums)
    key=0
    answer=S.deleteNode(S,root,key)