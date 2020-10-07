# @Date    : 21:23 09/28/2020
# @Author  : ClassicalPi
# @FileName: 33.py
# @Software: PyCharm

# class Solution:
#     def search(self, nums: [int], target: int) -> int:
#         for index,val in enumerate(nums):
#             if target==val:
#                 return index


class Solution:

    def binary_search_pivot(self,nums:[],left:int,right:int)->int:
        mid=(left+right)//2
        if right-left<=1:
            return mid
        if nums[mid]>=nums[left]:
            return self.binary_search_pivot(nums,mid,right)
        if nums[mid]<=nums[right]:
            return self.binary_search_pivot(nums,left,mid)

    def binary_search(self,nums:[],left:int,right:int,target)->int:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        if right-left<1:
            return -1
        if nums[mid]>target:
            return self.binary_search(nums,left,mid-1,target)
        else:
            return self.binary_search(nums,mid+1,right,target)

    def search(self, nums: [int], target: int) -> int:

        if not nums:
            return -1

        if len(nums)==1:
            if nums[0]==target:
                return 0
            return -1

        pivot=self.binary_search_pivot(nums,0,len(nums)-1)
        left=nums[0:pivot+1]
        right=nums[pivot+1:]

        ans=-1
        if target>=left[0]:
            ans=(self.binary_search(left,0,len(left)-1,target))
        if target<=right[-1] and ans==-1:
            ans=(self.binary_search(right,0,len(right)-1,target))
            if ans!=-1:
                ans+=len(left)
            return ans
        else:
            return ans


if __name__ == '__main__':
    S=Solution()
    print(S.search([1,3,5],3))