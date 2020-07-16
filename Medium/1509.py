# @Date    : 22:16 07/16/2020
# @Author  : ClassicalPi
# @FileName: 1509.py
# @Software: PyCharm
import random
class Solution:
    def minDifference(self, nums: [int]) -> int:
        if not nums:
            return 0
        # 1,2,3,4
        if len(nums)<=4:
            return 0
        # 1,2,3,4,5
        if len(nums)==5:
            nums=sorted(nums)
            return min((nums[-1]-nums[-2]),(nums[1]-nums[0]))
        else:
            # [6,6,0,1,1,4,6]
            nums=sorted(nums)
            res=[]
            for i in range(1,5):
                right=nums[0-i]
                left=nums[4-i]
                res.append(right-left)
            return min(res)
if __name__ == '__main__':
    S=Solution()
    print(S.minDifference([5,3,2,4]))
    print(S.minDifference([1,5,0,10,14]))
    print(S.minDifference([6,6,0,1,1,4,6]))
    print(S.minDifference([1,5,6,14,15]))