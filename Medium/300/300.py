# @Date    : 18:00 07/26/2021
# @Author  : ClassicalPi
# @FileName: 300.py
# @Software: PyCharm
import collections
import bisect
class Solution:
    # DP
    # def lengthOfLIS(self, nums: [int]) -> int:
    #     nums = nums[::-1]
    #     interRes = collections.defaultdict(int)
    #     for index,num in enumerate(nums):
    #         count = [0]
    #         for num2 in nums[0:index]:
    #             if num2 > num:
    #                 count.append(interRes[num2])
    #         interRes[num] = max(count)+1
    #     return max(list(interRes.values()))

    # BS
    def lengthOfLIS(self, nums: [int]) -> int:
        piles = []
        for num in nums:
            index = bisect.bisect_left(piles,num)
            if index+1 > len(piles):
                piles.append(num)
            else:
                piles[index] = num
        return len(piles)
if __name__ == '__main__':
    S=Solution()
    print(S.lengthOfLIS([10,9,2,5,3,7,101,18]))
    print(S.lengthOfLIS([0,1,0,3,2,3]))
    print(S.lengthOfLIS([7,7,7,7,7,7,7]))