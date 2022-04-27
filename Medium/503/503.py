# @Date    : 10:48 04/27/2022
# @Author  : ClassicalPi
# @FileName: 503.py
# @Software: PyCharm
class Solution:
    def nextGreaterElements(self, nums: [int]) -> [int]:
        extended_nums = nums.copy()
        extended_nums.extend(extended_nums[0:len(nums)-1])
        mono_stack = []
        order_dic = {}
        for index, val in enumerate(extended_nums):
            while mono_stack and mono_stack[-1][1] < val:
                order_dic.setdefault(mono_stack[-1][0], val)
                mono_stack.pop()
            mono_stack.append((index, val))
        for index, val in enumerate(nums):
            nums[index] = order_dic.get(index, -1)
        return nums

if __name__ == '__main__':
    S = Solution()
    print(S.nextGreaterElements([1,2,1]))