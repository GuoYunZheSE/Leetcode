# @Date    : 00:27 08/07/2020
# @Author  : ClassicalPi
# @FileName: 18.py
# @Software: PyCharm

import collections

class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        def threeSum(subNums:[],subTarget:int)->[[int]]:
            res=[]
            for i in range(0,len(subNums)-2):
                if subNums[i]==subNums[i-1] and i>0:
                    continue
                else:
                    left=i+1
                    right=len(subNums)-1
                    while left<right:
                        AddUp=subNums[i]+subNums[left]+subNums[right]
                        if AddUp<subTarget:
                            left+=1
                        elif AddUp==subTarget:
                            res.append([subNums[i],subNums[left],subNums[right]])
                            while left < right and subNums[left] == subNums[left + 1]:
                                left += 1
                            while left < right and subNums[right] == subNums[right - 1]:
                                right -= 1
                            left += 1
                            right -= 1
                        else:
                            right-=1
            return res
        nums.sort()
        res=[]
        for i in range(0,len(nums)-3):
            if nums[i]==nums[i-1] and i>0:
                continue
            temp=threeSum(nums[i+1:],target-nums[i])
            if temp:
                for each in temp:
                    each.append(nums[i])
            res.extend(temp)
        return res

if __name__ == '__main__':
    S=Solution()
    print(S.fourSum([1, 0, -1, 0, -2, 2, 2, 4, 2, 1, -423, -2, -434],0))