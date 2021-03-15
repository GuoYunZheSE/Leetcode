# @Date    : 10:54 03/15/2021
# @Author  : ClassicalPi
# @FileName: BitMask.py
# @Software: PyCharm
class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        n = len(nums)
        output = []

        for i in range(2 ** n, 2 ** (n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return output
if __name__ == '__main__':
    S=Solution()
    print(S.subsets([1,2,3]))