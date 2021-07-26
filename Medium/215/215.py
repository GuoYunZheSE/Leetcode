# @Date    : 16:05 04/26/2021
# @Author  : ClassicalPi
# @FileName: 215.py
# @Software: PyCharm
import random
class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        if not nums:
            return []
        pivot=random.choice(nums)
        left=[]
        mid=[]
        right=[]
        for num in nums:
            if num<pivot:
                left.append(num)
            elif num==pivot:
                mid.append(num)
            else:
                right.append(num)
        if k <= len(right):
            return self.findKthLargest(right,k)
        elif k> len(right)+len(mid):
            return self.findKthLargest(left,k-len(right)+len(mid))
        else:
            return mid[0]