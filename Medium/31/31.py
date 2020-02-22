import typing
import sys
class Solution:

    def list_difference(self,before:typing.List[int],after:typing.List[int])->int:
        dif=[after[i]-before[i] for i in range(0,len(before))]
        res=0
        count=0
        for i in dif[::-1]:
            res+=i*(10**count)
            count+=1
        return res
    def nextPermutation(self, nums: typing.List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        find=False
        minI=-1
        minJ=0
        aps=[]
        for i in range(len(nums)-1,0,-1):
            j=i-1
            while j > -1:
                if nums[i]>nums[j]:
                    find=True
                    minJ=j
                    minI=i
                    break
                else:
                    j-=1
            if find:
                for m in range(j+1,i+1):
                    if nums[m]>nums[j]:
                        if nums[m]<nums[minI]:
                            minI=m
                break

        if not find:
            nums.sort()
        else:
            nums[minI], nums[minJ] = nums[minJ], nums[minI]
            nums[minJ + 1:] = aps
            return
if __name__ == '__main__':
    nums=[20,28,29,10,21,13,24,18,25,28,12,2,20,16,13,6,21,20,25,17,24,2,10,0,13,13,19,10,4,3,13,24,2,4,5,23,18,21,11,13,11,15,8,1,23,13,29,7,25,24,24]
    s=Solution()
    s.nextPermutation(nums)
    print(nums)