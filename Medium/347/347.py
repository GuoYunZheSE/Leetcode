# @Date    : 00:02 08/12/2021
# @Author  : ClassicalPi
# @FileName: 347.py
# @Software: PyCharm
import collections
import heapq
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        dic = collections.Counter(nums)
        freques = [i*-1 for i in list(dic.values())]
        heapq.heapify(freques)
        resFreq = 0
        while k > 0:
            if len(freques) == 0:
                return [-1]
            resFreq = heapq.heappop(freques)
            k -= 1
        res = []
        for key,val in dic.items():
            if dic[key] >= resFreq*(-1):
                res.append(key)
        return res
if __name__ == '__main__':
    S = Solution()
    print(S.topKFrequent([3,0,1,0],1))