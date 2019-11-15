class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        stack = []
        lower = TreeNode(float('-inf'))
        nodes = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            top = stack.pop()

            if top.val < lower.val:
                nodes += [lower, top]
            lower = top

            if top.right:
                root = top.right

        if len(nodes) == 2:
            nodes[0].val, nodes[1].val = nodes[1].val, nodes[0].val
        elif len(nodes) == 4:
            nodes[0].val, nodes[3].val = nodes[3].val, nodes[0].val