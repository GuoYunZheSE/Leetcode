class Solution:
    def wiggleSort(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return nums
        if len(nums)==2:
            if nums[0]>nums[1]:
                nums[0],nums[1]=nums[1],nums[0]
            return nums
        for i in range(0,len(nums)-1):
            if i % 2==0:
                if nums[i]>=nums[i+1]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]

            else:
                if nums[i]<=nums[i+1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums
if __name__ == '__main__':
    nums=[1, 3, 2, 2, 3, 1]
    S=Solution()
    print(S.wiggleSort(nums))