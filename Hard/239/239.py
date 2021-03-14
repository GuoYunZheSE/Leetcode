# @Date    : 21:31 03/13/2021
# @Author  : ClassicalPi
# @FileName: 239.py
# @Software: PyCharm
import collections
class Solution:
    def maxSlidingWindow(self, nums, k):
        window=collections.deque()
        res=[]
        for index,val in enumerate(nums):
            while window and nums[window[-1]]<val:
                window.pop()
            window.append(index)
            if window[0]==index-k:
                window.popleft()
            if index>=k-1:
                res.append(nums[window[0]])
        return res
if __name__ == '__main__':
    S=Solution()
    print(S.maxSlidingWindow([1,2,4,2,1,24],2))