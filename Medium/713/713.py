# @Date    : 16:38 04/15/2021
# @Author  : ClassicalPi
# @FileName: 713.py
# @Software: PyCharm
import collections
class Solution:
    # O(n2)
    # def numSubarrayProductLessThanK(self, nums: [int], k: int) -> int:
    #     res=0
    #     for i in range(0,len(nums)-1):
    #         product=nums[i]
    #         if product<k:
    #             res+=1
    #         else:
    #             continue
    #         for j in range(i+1,len(nums)):
    #             product*=nums[j]
    #             if product < k:
    #                 res += 1
    #             else:
    #                 break
    #     return res
    # O(n)
    def numSubarrayProductLessThanK(self, nums: [int], k: int) -> int:
        window=collections.deque()
        res=0
        product = 1
        for num in nums:
            while product*num>=k and window:
                res+=len(window)
                product=int(product/window.popleft())
            if product*num<k:
                window.append(num)
                product*=num
        return res+int((len(window)+1)*len(window)/2)
if __name__ == '__main__':
    S=Solution()
    print(S.numSubarrayProductLessThanK([10, 5, 2, 6],100))
