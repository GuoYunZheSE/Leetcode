# @Date    : 20:37 08/01/2020
# @Author  : ClassicalPi
# @FileName: 15.py
# @Software: PyCharm
from bisect import bisect_left,bisect_right
class Solution:
    # def threeSum(self, nums: [int]) -> [[int]]:
    #     res=[]
    #     ans=[]
    #     s=set()
    #     if len(nums)<=2:
    #         return []
    #     for i in range(0,len(nums)-1):
    #         for j in range(i+1,len(nums)):
    #             res.append((nums[i]+nums[j],i,j))
    #     for each in res:
    #         for index,val in enumerate(nums[each[2]+1:]):
    #             if val==(-each[0]):
    #                 temp=sorted([nums[each[1]], nums[each[2]], nums[index + each[2]+1]])
    #                 temp_str=""
    #                 for i in temp:
    #                     temp_str+=f"{i}"
    #                 if temp_str not in s:
    #                     ans.append(temp)
    #                     s.add(temp_str)
    #     return ans
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
if __name__ == '__main__':
    S=Solution()
    print(S.threeSum([1, 0, -1, 0, -2, 2, 2, 4, 2, 1, -423, -2, -434]))