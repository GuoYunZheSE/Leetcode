# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums=[]
        self.mins=[]

    def push(self, x: int) -> None:
        self.nums.append(x)
        if self.mins==[]:
            self.mins.append(x)
        else:
            if self.mins[-1]<=x:
                self.mins.append(self.mins[-1])
            else:
                self.mins.append(x)
    def pop(self) -> None:
        if len(self.nums)>0:
            self.nums.pop()
            self.mins.pop()
    def top(self) -> int:
        if len(self.nums)>0:
            return self.nums[-1]
    def getMin(self) -> int:
        if len(self.nums)>0:
            return self.mins[-1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()