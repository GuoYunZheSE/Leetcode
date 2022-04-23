# @Date    : 14:17 04/23/2022
# @Author  : ClassicalPi
# @FileName: 27.py
# @Software: PyCharm
class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        for hole in range(0, len(nums)):
            if nums[hole] == val:
                for j in range(hole + 1, len(nums)):
                    if nums[j] != val:
                        nums[hole],nums[j] = nums[j], nums[hole]
        return len(nums) - nums.count(val)

if __name__ == '__main__':
    S = Solution()
    print(S.removeElement([3,2,2,3],3))
    print(S.removeElement([0,1,2,2,3,0,4,2], 2))