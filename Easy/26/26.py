# @Date    : 21:51 09/20/2020
# @Author  : ClassicalPi
# @FileName: 26.py
# @Software: PyCharm

class Solution:
    def removeDuplicates(self, nums: [int]) -> int:

        length=0

        if len(nums)<=1:
            return len(nums)

        for i in range(0,len(nums)-1):

            if nums[i]!=nums[i+1]:

                nums[length]=nums[i]

                if i!=len(nums)-2:
                    length+=1

                else:
                    nums[length+1] = nums[i+1]
                    length+=2
            else:
                if i==len(nums)-2:
                    nums[length] = nums[i+1]
                    length+=1
        print(nums)
        return length

if __name__ == '__main__':
    S=Solution()
    print(S.removeDuplicates([1,2,3,4,5,6,6,6,6,7,7,7,7,8,8,8,10,10]))