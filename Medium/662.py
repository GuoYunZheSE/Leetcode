# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x,l,r):
        self.val = x
        self.left = l
        self.right = r

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

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 0, 0)]
        curdepth, pos, res = 0, 0, 0
        left = 0
        for node, depth, pos in stack:
            if node:
                stack.append((node.left, depth + 1, pos * 2))
                stack.append((node.right, depth + 1, pos * 2 + 1))
                if curdepth != depth:
                    curdepth = depth
                    left = pos
                res = max(res, pos - left + 1)
        return res
    # Time Limit Exceeded
    # def widthOfBinaryTree(self, root: TreeNode) -> int:
    #     if root.val is None:
    #         return 0
    #
    #     levels=[[root.val]]
    #     now=[root]
    #     while True:
    #         next = []
    #         detail = []
    #         for eachnode in now:
    #             if eachnode is not None:
    #                 next.append(eachnode.left)
    #                 next.append(eachnode.right)
    #                 if eachnode.left is None:
    #                     detail.append(None)
    #                 else:
    #                     detail.append(eachnode.left.val)
    #                 if eachnode.right is None:
    #                     detail.append(None)
    #                 else:
    #                     detail.append(eachnode.right.val)
    #             if eachnode is None:
    #                 next.append(TreeNode(None,None,None))
    #                 next.append(TreeNode(None,None,None))
    #                 detail.append(None)
    #                 detail.append(None)
    #         now=next
    #         if detail.count(None)==len(detail):
    #             break
    #         levels.append(detail)
    #
    #     width=[]
    #     for eachlevel in levels:
    #         temp=eachlevel[::-1]
    #         begin=0
    #         end=len(temp)
    #         count1=0
    #         count2=0
    #         for y in eachlevel:
    #             if y is not None:
    #                 begin=count1
    #                 break
    #             count1+=1
    #
    #         for j in temp:
    #             if j is not None:
    #                 end=count2
    #                 break
    #             count2+=1
    #         width.append(len(eachlevel)-begin-end)
    #     return max(width)
if __name__ == '__main__':
    # S=TreeNode(1,TreeNode(3,TreeNode(5,TreeNode(6,None,None),TreeNode(None,None,None)),TreeNode(None,None,None)),TreeNode(2,TreeNode(None,None,None),TreeNode(9,TreeNode(None,None,None),TreeNode(7,None,None))))
    S=TreeNode(1,TreeNode(3,TreeNode(6,None,None),TreeNode(7,None,None)),TreeNode(5,TreeNode(None,None,None),TreeNode(9,None,None)))
    A=Solution()
    print(A.widthOfBinaryTree(S))


