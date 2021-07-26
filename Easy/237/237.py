# @Date    : 23:57 07/18/2021
# @Author  : ClassicalPi
# @FileName: 237.py
# @Software: PyCharm
def deleteNode(self, node):
    node.val = node.next.val
    node.next = node.next.next