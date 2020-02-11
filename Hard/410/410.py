class Solution:
    def splitArray(self, nums: [int], m: int) -> int:
        status=[[],sum(nums),0]
        dict={
            0:nums
        }