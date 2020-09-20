# @Date    : 21:33 08/10/2020
# @Author  : ClassicalPi
# @FileName: 1.py
# @Software: PyCharm

class Tree:

    def __init__(self, val=0):
        self.val = val
        self.child=[]

    def insert_child(self, c):
        self.child.append(c)


# def tree_to_list_by_queue(root: Tree) -> list:  # 队列实现层次遍历（非递归）
#     num_list = []
#     if not root:
#         return
#     myQueue = list()
#     myQueue.append(root)
#     while myQueue:
#         node = myQueue.pop(0)
#         num_list.append(node.val)
#         for child in node.child:
#             if child:
#                 myQueue.append(child)
#     return num_list


if __name__ == '__main__':
    while True:
        count = int(input())
        s2 = input().split()
        s3 = input().split()
        val = list()
        parents = list()
        Tree_list = list()
        for i in s2:
            val.append(int(i))
        for i in s3:
            parents.append(int(i))
        if count > 0:
            root = Tree(val[0])
            Tree_list.append(root)
        for i in range(1, count):
            if i > parents[i - 1]:
                child_node = Tree(val[i])
                parents_node = Tree_list[parents[i - 1]]
                parents_node.insert_child(child_node)
                Tree_list.append(child_node)
            else:
                print('Parent not exist!')
        print(root)