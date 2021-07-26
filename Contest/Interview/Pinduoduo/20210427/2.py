# @Date    : 19:44 04/27/2021
# @Author  : ClassicalPi
# @FileName: 2.py
# @Software: PyCharm
import sys
class Solution:
    def reverseList(self,nums:list):
        zero=nums.count(0)
        one=len(nums)-zero
        for i in range(0,len(nums)):
            if i==0:
                nums[i]=-1 if nums[i]==1 else 1
            else:
                if nums[i-1]>=0:
                    if nums[i]==1:
                        nums[i]=nums[i-1]-1
                    else:
                        nums[i] = nums[i - 1] + 1
                else:
                    nums[i]=-1 if nums[i]==1 else 1
        return max(one,one+max(nums))
if __name__ == '__main__':
    S=Solution()
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    print(S.reverseList(values))