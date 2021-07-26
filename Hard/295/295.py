# @Date    : 14:55 07/26/2021
# @Author  : ClassicalPi
# @FileName: 295.py
# @Software: PyCharm
import collections
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dic = collections.defaultdict(int)
        self.total = 0
    def addNum(self, num: int) -> None:
        self.dic[num]+=1
        self.total+=1
    def findMedian(self) -> float:
        if self.total %2 != 0:
            target1 = self.total//2
            target2 = self.total//2
        else:
            target1 = self.total // 2
            target2 = (self.total // 2) - 1
        res = []
        found1 = False
        found2 = False
        for key,val in self.dic.items():
            if target1 <= 0 and not found1:
                res.append(key)
                found1 = True
            if target2 <= 0 and not found2:
                res.append(key)
                found2 = True
            if target1 > 0:
                target1 -= val
            if target2 > 0:
                target2 -= val
            if found2 and found1:
                break
        print(res)
        return sum(res)/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

if __name__ == '__main__':
    S=MedianFinder()
    S.addNum(1)
    S.addNum(2)
    print(S.findMedian())