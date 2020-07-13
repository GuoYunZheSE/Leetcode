# @Date    : 22:44 07/11/2020
# @Author  : ClassicalPi
# @FileName: 5445.py
# @Software: PyCharm

# Given the array nums consisting of n positive integers. You computed the sum of all non-empty continous subarrays from the array and then sort them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.
#
# Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 10^9 + 7.

class Solution:
    def rangeSum(self, nums: [int], n: int, left: int, right: int) -> int:
        res=[]
        table={}
        s=0
        for i in range(0,len(nums)):
            s+=nums[i]
            table.setdefault(i,s)
            res.append(s)
        temp=[]
        temp+=res
        for i in range(1,len(nums)):
            res+=[a-temp[i-1] for a in temp[i:]]
        return sum(sorted(res)[left-1:right])
if __name__ == '__main__':
    S=Solution()
    print(S.rangeSum([1,2,3,4],4,1,5))
    print(S.rangeSum([1, 2, 3, 4], 4, 3, 4))
    print(S.rangeSum([1, 2, 3, 4], 4, 1, 10))
    print(S.rangeSum([1, 2, 3, 4], 4, 1, 9))