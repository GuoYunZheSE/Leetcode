class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def sortedArrayToBST(self, nums):
        if nums == [] or nums == None:
            return None
        root = TreeNode(0)
        stack = [[0, len(nums) - 1, root]]
        while (len(stack)):
            left, right, node = stack.pop()
            middle = (left + right) // 2
            node.val = nums[middle]
            if left <= middle - 1:
                node.left = TreeNode(0)
                stack.append([left, middle - 1, node.left])
            if right >= middle + 1:
                node.right = TreeNode(0)
                stack.append([middle + 1, right, node.right])
        return root