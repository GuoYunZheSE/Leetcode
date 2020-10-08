# @Date    : 12:29 10/07/2020
# @Author  : ClassicalPi
# @FileName: 287.py
# @Software: PyCharm

# import collections
# class Solution:
#     def findDuplicate(self, nums: [int]) -> int:
#         num_dict=collections.Counter(nums)
#         for key,val in num_dict.items():
#             if val>=2:
#                 return key

class Solution:
    def findDuplicate(self, nums: [int]) -> int:

        # Find the meeting point
        faster=nums[nums[0]]
        slower=nums[0]
        while faster!=slower:
            faster=nums[nums[faster]]
            slower=nums[slower]

        # Locate the meeting point
        faster=0
        while faster!=slower:
            faster=nums[faster]
            slower=nums[slower]
        return faster
if __name__ == '__main__':
    S=Solution()
    print(S.findDuplicate([3,1,3,2,4]))