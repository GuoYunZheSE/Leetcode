# @Date    : 12:11 04/15/2021
# @Author  : ClassicalPi
# @FileName: 152.py
# @Software: PyCharm
import sys
class Solution:
    def maxProduct(self, nums: [int]) -> int:
        MAX=nums[0]
        MIN=nums[0]
        res=-sys.maxsize
        for i in range(1,len(nums)):
            max_product=MAX*nums[i]
            min_product=MIN*nums[i]
            MAX=max(max_product,min_product,nums[i])
            MIN=min(max_product,min_product,nums[i])
            res=max(res,MAX)
        return res
if __name__ == '__main__':
    S=Solution()
    print(S.maxProduct([1,2,4,12,4,231,-2,12,-5,2,0,4]))