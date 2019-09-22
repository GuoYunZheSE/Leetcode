# 1054. Distant Barcodes
# Medium
# In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].
# Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists.
import heapq
class Solution:
    def __init__(self):
        self.dic={}
    def rearrangeBarcodes(self, barcodes: [int]) -> [int]:
        if len(barcodes)<=2:
            return barcodes
        for i in barcodes:
            if self.dic.__contains__(i):
                temp=self.dic[i]
                self.dic.update({i:temp+1})
            else:
                self.dic.setdefault(i,0)
        minHeap=[(-v,k) for k,v in self.dic.items()]
        heapq.heapify(minHeap)
        res=[]
        while minHeap:
            if len(minHeap)>=2:

                v1,k1=heapq.heappop(minHeap)
                v2, k2 = heapq.heappop(minHeap)
                res.append(k1)
                res.append(k2)
                if v1<=-1:
                    heapq.heappush(minHeap,(v1+1,k1))
                if v2<=-1:
                    heapq.heappush(minHeap,(v2+1,k2))
            else:
                v1, k1 = heapq.heappop(minHeap)
                if v1<=-1:
                    heapq.heappush(minHeap,(v1+1,k1))
                res.append(k1)
        return res
if __name__ == '__main__':
    S=[1,1,1,1,2,2,3,3]
    A=Solution()
    print(A.rearrangeBarcodes(S))

