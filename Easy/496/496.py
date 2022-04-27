# @Date    : 18:19 04/26/2022
# @Author  : ClassicalPi
# @FileName: 496.py
# @Software: PyCharm
# class Solution:
#     def nextGreaterElement(self, nums1: [int], nums2: [int]) -> [int]:
#         res = []
#         maxNum = max(nums2)
#         nums2_dict = {}
#         for i in range(len(nums2)):
#             nums2_dict.setdefault(nums2[i],i)
#
#         for num in nums1:
#             if num >= maxNum:
#                 res.append(-1)
#             else:
#                 found = False
#                 for i in range(nums2_dict[num],len(nums2)):
#                     if nums2[i] > num:
#                         res.append(nums2[i])
#                         found = True
#                         break
#                 if not found:
#                     res.append(-1)
#         return res


class Solution:
    def nextGreaterElement(self, nums1: [int], nums2: [int]) -> [int]:
        nextGreaterDict = {}
        monoStack = []

        for num in nums2:
            while monoStack and num > monoStack[-1]:
                nextGreaterDict[monoStack.pop()] = num
            monoStack.append(num)

        for i, num in enumerate(nums1):
            nums1[i] = nextGreaterDict.get(num, -1)

        return nums1
if __name__ == '__main__':
    S = Solution()
    print(S.nextGreaterElement( nums1 = [4,1,2], nums2 = [1,3,4,2]))