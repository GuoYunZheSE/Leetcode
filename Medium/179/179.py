import typing
import Util.Sort as us
class LargerNumKey(str):
    def __lt__(self, other):
        return self+other > other+self

class Solution:
    def largestNumber(self, nums: [int]) -> str:
        if not nums:
            return ""
        nums.sort(key=LargerNumKey)
        res=""
        if nums[0]==0:
            return "0"
        for each in nums:
            res+="{}".format(each)
        return res

if __name__ == '__main__':
    nums=[10,2]
    S=Solution()
    S.largestNumber(nums)