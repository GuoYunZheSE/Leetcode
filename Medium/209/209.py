import typing
import sys
class Solution:
    def minSubArrayLen(self, s: int, nums: typing.List[int]) -> int:
        left,right=0,0
        res,cur=sys.maxsize,0
        for right in range(0,len(nums)):
            cur+=nums[right]
            while cur>=s:
                if cur-nums[left]>=s:
                    cur-=nums[left]
                    left+=1
                else:
                    res = min(res, right - left + 1)
                    break
        if res==sys.maxsize:
            res=0
        return res

if __name__ == '__main__':
    s = Solution()
    n = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(s.minSubArrayLen(n, nums))