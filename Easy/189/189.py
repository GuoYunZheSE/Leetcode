# @Date    : 08:17 03/31/2020
# @Author  : ClassicalPi
# @FileName: 189.py
# @Software: PyCharm

import timeit
class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        nums[:]=nums[len(nums)-k:]+nums[0:len(nums)-k]
        print(nums)

if __name__ == '__main__':
    nums= [1,2,3,4,5,6,7]
    k =3
    s=Solution()
    print(s.rotate(nums,k))