import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smaller = []
        self.bigger = []

    def addNum(self, num: int) -> None:
        if len(self.bigger) > len(self.smaller):
            heapq.heappush(self.smaller,-heapq.heappushpop(self.bigger,num))
        else:
            heapq.heappush(self.bigger,-heapq.heappushpop(self.smaller,-num))
    def findMedian(self) -> float:
        if len(self.smaller) == len(self.bigger):
            return (self.bigger[0] - self.smaller[0])/2
        else:
            return self.bigger[0]