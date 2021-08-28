# @Date    : 16:10 08/14/2021
# @Author  : ClassicalPi
# @FileName: 378.py
# @Software: PyCharm
import heapq
class Solution:
    def kthSmallest(self, matrix: [[int]], k: int) -> int:
        res = []
        for row in matrix:
            for number in row:
                if len(res) < k:
                    heapq.heappush(res,number*(-1))
                else:
                    heapq.heappushpop(res,number*(-1))
        return res[0] * (-1)