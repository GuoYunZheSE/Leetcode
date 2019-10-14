class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        max_ending_here = max_so_far =nums[0]
        for x in nums[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
if __name__ == '__main__':
    S=Solution()
    print(S.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))