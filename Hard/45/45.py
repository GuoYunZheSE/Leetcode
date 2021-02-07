# @Date    : 17:57 02/07/2021
# @Author  : ClassicalPi
# @FileName: 45.py
# @Software: PyCharm
import sys
class Solution:
    def jump(self, nums: [int]) -> int:
        steps=[sys.maxsize]*len(nums)
        steps[-1]=-1
        for i in range(len(nums)-1,-1,-1):
            steps[i]=min(steps[i:min(i+nums[i],len(nums))+1])+1
        return steps[0]

if __name__ == '__main__':
    S=Solution()
    print(S.jump([2,3,0,1,4]))