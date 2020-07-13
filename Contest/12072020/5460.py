# @Date    : 10:30 07/12/2020
# @Author  : ClassicalPi
# @FileName: 5460.py
# @Software: PyCharm

class Solution:
    def numIdenticalPairs(self, nums: [int]) -> int:
        res=0
        for index1,val1 in enumerate(nums):
            for index2 in range(index1,len(nums)):
                if index2!=index1 and val1==nums[index2]:
                    res+=1
        return res


if __name__ == '__main__':
    S=Solution()
    print(S.numIdenticalPairs([1,2,3,1,1,3]))
    print(S.numIdenticalPairs([1,1,1,1]))
    print(S.numIdenticalPairs([1, 2, 3]))