# @Date    : 18:49 05/23/2020
# @Author  : ClassicalPi
# @FileName: 225.py
# @Software: PyCharm

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=[]

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        res=-1
        if not self.empty():
            res=self.stack[-1]
            self.stack=self.stack[0:len(self.stack)-1:1]
        return res
    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.empty():
            return self.stack[-1]
        else:
            return -1

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.stack==[]:
            return True
        else:
            return False