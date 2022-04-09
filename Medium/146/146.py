class Node:
    def __init__(self,val):
        self.val = val
        self.pre = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.memory_map = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.memory_list = Node(0)
        self.head.next = self.memory_list
        self.memory_list.pre = self.head
        self.memory_list.next = self.tail
        self.tail.pre = self.memory_list
    def get(self, key: int) -> int:
        if key in self.memory_map:
            N = self.memory_map[key]
            N.pre.next = N.next
            N.next.pre = N.pre
            N.next = self.head.next
            self.head.next = N
            N.next.pre = N
            N.pre = self.head
            return N.val
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.memory_map:
            N = self.memory_map[key]
            N.pre.next = N.next
            N.next.pre = N.pre
            N.next = self.head.next
            self.head.next = N
            N.next.pre = N
            N.pre = self.head
            N.val = value
            return
        else:
            if self.capacity == 0:
                N = self.tail.pre
                N.pre.next = self.tail
                self.tail.pre = N.pre
                del N
                self.capacity += 1
            N = Node(value)
            self.memory_map[key] = N
            N.next=self.head.next
            self.head.next.pre = N
            N.pre = self.head
            self.head.next = N
            self.capacity -= 1
            return