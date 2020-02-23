import typing
import sys


class Solution:
    def nextPermutation(self, nums: typing.List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1. check from end if any number is in decreasing order.
        2. If not found then just reverse whole and return.
        3. Now check number which is larger than the found number which was in decreasing order, swap with it.
        4. now reverse whole from the next index  as we want the smallest permutation as it is strictly increasing.
        """
        i = j = len(nums) - 1

        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        ##checking if i is 0, if it is just reverse the list and return
        if i == 0:
            nums.reverse()
            return

        k = i - 1  ## our target number index
        while nums[j] <= nums[k]:
            j -= 1

        ## now swap numbers
        nums[j], nums[k] = nums[k], nums[j]

        ## now reverse the left list
        left, right = k + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    nums=[4,2,0,2,3,2,0]
    s=Solution()
    s.nextPermutation(nums)
    print(nums)