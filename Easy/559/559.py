# @Date    : 10:59 03/25/2021
# @Author  : ClassicalPi
# @FileName: 559.py
# @Software: PyCharm

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.max_depth=0
    def DFS(self,root:Node,depth:int):
        if root.children is None:
            self.max_depth=max(self.max_depth,depth)
        else:
            for child in root.children:
                self.DFS(child,depth+1)
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        self.DFS(root,1)
        return self.max_depth

if __name__ == '__main__':
    S=Solution()
    N1=Node(1)
    N2 = Node(2)
    N3 = Node(3)
    N4 = Node(4)
    N5 = Node(5)
    N6 = Node(6)
    N1.children=[N3,N2,N4]
    N3.children=[N5,N6]
    print(S.maxDepth(N1))
