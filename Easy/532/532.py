# 532. K-diff Pairs in an Array
# Runtime: 44 ms, faster than 96.87% of Python3 online submissions for K-diff Pairs in an Array.
# Memory Usage: 15.8 MB, less than 7.71% of Python3 online submissions for K-diff Pairs in an Array.

import collections
class Solution:
    def findPairs(self, nums: list, k: int) -> int:
        if k>0:
            return len(set(nums)&set(n+k for n in nums))
        elif k==0:
            return (sum(v>1 for v in collections.Counter(nums).values()))
        else:
            return 0
if __name__ == '__main__':
    numbers=[1,3,1,4,5]
    k=2
    S=Solution()
    A=S.findPairs(numbers,k)
    print(A)