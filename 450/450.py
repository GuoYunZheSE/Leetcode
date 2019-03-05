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
            root.left = self.deleteNode(self,root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(self,root.right, key)
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
    def deleteNode(self, root, key):
        if not root: # if root doesn't exist, just return it
            return root
        if root.val > key: # if key value is less than root value, find the node in the left subtree
            root.left = self.deleteNode(root.left, key)
        elif root.val < key: # if key value is greater than root value, find the node in right subtree
            root.right= self.deleteNode(root.right, key)
        else: #if we found the node (root.value == key), start to delete it
            if not root.right: # if it doesn't have right children, we delete the node then new root would be root.left
                return root.left
            if not root.left: # if it has no left children, we delete the node then new root would be root.right
                return root.right
                   # if the node have both left and right children,  we replace its value with the minmimum value in the right subtree and then delete that minimum node in the right subtree
            temp = root.right
            mini = temp.val
            while temp.left:
                temp = temp.left
                mini = temp.val
            root.val = mini # replace value
            root.right = self.deleteNode(root.right,root.val) # delete the minimum node in right subtree
        return root
if __name__ == '__main__':
    S=Solution
    nums=[0,1,2,3,4,5,6,7,8,9]
    root=S.sortedArrayToBST(S,nums)
    key=3
    answer=S.deleteNode(S,root,key)