import sys
import collections
class Solution:
    # O(nlogn)
    def longestConsecutive(self, nums: [int]) -> int:
        if len(nums)<2:
            return len(nums)
        nums=sorted(nums)
        window=collections.deque()
        i=0
        res=-sys.maxsize
        while i<len(nums):
            if not window:
                window.append(nums[i])
            else:
                while i<len(nums):
                    if nums[i] == window[-1] + 1:
                        window.append(nums[i])
                        i += 1
                    elif nums[i] == window[-1]:
                        i+=1
                    else:break
                res=max(res,len(window))
                if i<len(nums):
                    window=collections.deque([nums[i]])
            i+=1
        return res
    # O(n)
    def longestConsecutive2(self, nums: [int]) -> int:
        if len(nums)<2:
            return len(nums)
        nums=sorted(nums)
        window=collections.deque()
        i=0
        res=-sys.maxsize
        while i<len(nums):
            if not window:
                window.append(nums[i])
            else:
                while i<len(nums):
                    if nums[i] == window[-1] + 1:
                        window.append(nums[i])
                        i += 1
                    elif nums[i] == window[-1]:
                        i+=1
                    else:break
                res=max(res,len(window))
                if i<len(nums):
                    window=collections.deque([nums[i]])
            i+=1
        return res