# @Date    : 23:26 08/10/2021
# @Author  : ClassicalPi
# @FileName: 334.py
# @Software: PyCharm
import bisect
class Solution:
    def increasingTriplet(self, nums: [int]) -> bool:
        piles = []
        for num in nums:
            index = bisect.bisect_left(piles,num)
            if index + 1 > len(piles):
                piles.append(num)
            else:
                piles[index] = num
        return len(piles) >= 3