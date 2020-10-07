# @Date    : 11:16 09/27/2020
# @Author  : ClassicalPi
# @FileName: 5525.py
# @Software: PyCharm
class Node(object):
    '''定义单链表节点类'''
    def __init__(self,data,next = None):
        '''data为数据项，next为下一节点的链接，初始化节点默认链接为None'''
        self.data = data
        self.next = next
        self.died=False

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.family_tree=Node(kingName)
        self.death_list=[]
    def birth(self, parentName: str, childName: str) -> None:
        head=self.family_tree
        while head:
            if head.data==parentName:
                after=head.next
                head.next=Node(childName,after)
                return
            else:
                head=head.next
    def death(self, name: str) -> None:
        self.death_list.append(name)
    def getInheritanceOrder(self) -> [str]:
        res=[]
        head=self.family_tree
        while head:
            if head.data not in self.death_list:
                res.append(head.data)
            head=head.next
        return res

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

if __name__ == '__main__':
    t = ThroneInheritance("king")
    t.birth("king", "andy")
    t.birth("king", "bob")
    t.birth("king", "catherine")
    t.birth("andy", "matthew")
    t.birth("bob", "alex")
    t.birth("bob", "asha")
    print(t.getInheritanceOrder())
    t.death("bob")
    print(t.getInheritanceOrder())