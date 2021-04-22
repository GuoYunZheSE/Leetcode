# @Date    : 15:30 04/15/2021
# @Author  : ClassicalPi
# @FileName: 198.py
# @Software: PyCharm
class Solution:
    def rob(self, nums: [int]) -> int:
        dp=[0 for i in range(0,len(nums)+3)]
        # 0 0 0 1 2 3 1
        for i in range(0,len(nums)):
            dp[i+3]=max(dp[i+1],dp[i])+nums[i]
        return max(dp)
if __name__ == '__main__':
    S=Solution()
    print(S.rob([1,2,3,1]))
    print(S.rob( [2000,7,3,9000,1]))