# @Date    : 15:29 04/23/2022
# @Author  : ClassicalPi
# @FileName: 732.py
# @Software: PyCharm
class MyCalendarThree:

    def __init__(self):
        self.events = []
    def book(self, start: int, end: int) -> int:
        self.events.append((start,1))
        self.events.append((end,0))
        self.events.sort()

        res, k = 0, 0
        for _, action in self.events:
            if action == 1:
                k += 1
            else:
                k -= 1
            if k > res:
                res = k
        return res