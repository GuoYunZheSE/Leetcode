# @Date    : 15:32 07/26/2021
# @Author  : ClassicalPi
# @FileName: 297.py
# @Software: PyCharm
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
import random
class Codec:
    def serialize(self, root:TreeNode)->str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def PreOrder(root:TreeNode,Trace:[],TraceSet:set):
            if root.val in TraceSet:
                root.val = str(root.val)+"_"+str(random.randint(0,99999))
                Trace.append(root.val)
            else:
                TraceSet.add(root.val)
                Trace.append(str(root.val))
            if root.left:
                PreOrder(root.left,Trace,TraceSet)
            if root.right:
                PreOrder(root.right,Trace,TraceSet)

        def MidOrder(root:TreeNode,Trace:[],TraceSet:set):
            if root.left:
                MidOrder(root.left,Trace,TraceSet)
            Trace.append(str(root.val))
            if root.right:
                MidOrder(root.right,Trace,TraceSet)
        if not root:
            return ";;"
        preOrder = []
        midOrder = []
        PreOrder(root,preOrder,set())
        MidOrder(root,midOrder,set())
        return ",".join(preOrder)+";;"+",".join(midOrder)

    def deserialize(self, data:str)->TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # [1,2,3,4,5]
        # [2,1,4,3,5]
        def construct(mid:[])->TreeNode:
            if mid:
                root_val = self.preOrder.popleft()
                root_index = mid.index(root_val)
                root_node = TreeNode(int(root_val.split("_")[0]))
                root_node.left = construct(mid[:root_index])
                root_node.right = construct(mid[root_index+1:])
                return root_node
        if data == ";;":
            return None
        data = data.split(";;")
        self.preOrder, midOrder = data[0].split(","),data[1].split(",")
        self.preOrder = collections.deque(self.preOrder)
        return construct(midOrder)

if __name__ == '__main__':
    S=Codec()
    a=S.deserialize("1,2,3,4,5;;2,1,4,3,5")
    print("11")