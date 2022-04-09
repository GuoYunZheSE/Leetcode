# @Date    : 12:13 09/06/2021
# @Author  : ClassicalPi
# @FileName: BIgo.py
# @Software: PyCharm
# 1 2 3 4 5 6 7 8     3
# 3 2 1 6 5 4 7 8

class Node:
    def __init__(self):
        self.val = None
        self.next = None

def K_reverse(head: Node, k: int):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    res = []
    for i in range(0,len(vals)//k+1):
        res.extend(vals[i*k:i*k+k][::-1])
    head = Node()
    h = head
    for each in res:
        n = Node()
        n.val = each
        head.next = n
        head = head.next
    return h.next
if __name__ == '__main__':
    n1 = Node()
    n1.val = 1
    n2 = Node()
    n2.val = 2
    n3 = Node()
    n3.val = 3
    n4 = Node()
    n4.val = 4
    n5 = Node()
    n5.val = 5
    n6 = Node()
    n6.val = 6
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    res = K_reverse(n1,3)
    print(res)
