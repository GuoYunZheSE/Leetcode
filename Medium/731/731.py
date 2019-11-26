# #Method 1
# class MyCalendarTwo:
#
#     def __init__(self):
#         self.once=[]
#         self.twice=[]
#     def book(self, start: int, end: int) -> bool:
#         for s,e in self.twice:
#             if start<e and end>s:
#                 return False
#         for s, e in self.once:
#             if start<e and end>s:
#                 self.twice.append((max(start,s),min(e,end)))
#         self.once.append((start,end))
#         return True

class Node:
    def __init__(self,start:int,end:int,usetime:int):
        self.Left=None
        self.right=None
        self.start=start
        self.end=end
        self.useTime=usetime

    def use(self):
        self.useTime+=1
        return self.useTime

class MyCalendarTwo:

    def __init__(self):

    def book(self, start: int, end: int) -> bool:

    def insert(self, start:int, end:int, node:Node,usetime:int):

        if end<=node.start or start>=node.end:
            if start>=node.end:
                if node.right is not None:
                    self.insert(start, end, node.right,usetime)
                else:
                    # new node
                    node.right=Node(start,end,0)
                    return node.use()<=2
            else:
                if node.Left is not None:
                    self.insert(start, end, node.Left,usetime)
                else:
                    # new node
                    node.Left = Node(start, end,0)
                    return node.use() <= 2
        else:
            if start<node.start:
                if end<=node.end:
                    temp=node.end
                    node.end=end
                    return node.use() and self.insert(start,node.start,node,0) and self.insert(node.end,temp,node,1)

