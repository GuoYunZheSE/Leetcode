# @Date    : 22:34 08/05/2020
# @Author  : ClassicalPi
# @FileName: 16.py
# @Software: PyCharm

import collections
import sys
class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        res=[]
        if len(nums)==3:
            return sum(nums)
        nums.sort()
        for index,val in enumerate(nums):
            left=index+1
            right=len(nums)-1
            Difference=collections.deque([sys.maxsize])
            while left<right:
                S=val+nums[left]+nums[right]
                Difference.append(target-S)
                if target-S>0:
                    left+=1
                elif target-S<0:
                    right-=1
                else:
                    return target
            res.append([d for d in Difference if d==sorted(Difference,key=lambda x:abs(x))[0]][0])
        return target-sorted(res,key=lambda x:abs(x))[0]

if __name__ == '__main__':
    S=Solution()
    print(S.threeSumClosest(nums =     [1, 6, 9, 14, 16, 70], target = 81))
