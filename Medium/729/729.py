import bisect
class MyCalendar:

    # def __init__(self):
    #     self.left=None
    #     self.right=None
    #     self.available=[]
    # def book(self, start: int, end: int) -> bool:
    #     if (start and end) or (start==0 and end) :
    #         if start<=end:
    #             # First Book
    #             if self.left==None:
    #                 self.left=start
    #                 self.right=end
    #                 return True
    #             else:
    #                 if end<=self.left :
    #                     if end!=self.left:
    #                         self.available.append((end,self.left))
    #                     self.left=start
    #                     return True
    #                 if start>=self.right:
    #                     if start!=self.right:
    #                         self.available.append((self.right,start))
    #                     self.right=end
    #                     return True
    #                 else:
    #                     if len(self.available)>0:
    #                         for inter in self.available:
    #                             if inter[0]<=start and end<=inter[1]:
    #                                 self.available.remove(inter)
    #                                 if inter[0]!=start:
    #                                     self.available.append((inter[0],start))
    #                                 if inter[1]!=end:
    #                                     self.available.append((end,inter[1]))
    #                                 return True
    #                         return False
    #                     return False
    #         else:
    #             return False
    #     else:
    #         return False

    def __init__(self):
        self.arr = []
        self.dict = {}

    def book(self, start: int, end: int) -> bool:
        if start in self.dict:
            return False
        if not self.arr:
            self.arr.append(start)
            self.dict[start] = end
            return True

        i = bisect.bisect_left(self.arr, start)
        if i - 1 >= 0 and self.dict[self.arr[i - 1]] > start:
            return False
        if i < len(self.arr) and self.arr[i] < end:
            return False

        self.arr.insert(i, start)
        self.dict[start] = end
        return True
if __name__ == '__main__':
    S=MyCalendar()
    S.book(48,50)
    print(S.book(0,6))