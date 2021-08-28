# @Date    : 16:33 08/14/2021
# @Author  : ClassicalPi
# @FileName: 384.py
# @Software: PyCharm
import random
class Solution:
    def __init__(self, nums: [int]):
        self.origin = [i for i in nums]
        self.cur = [i for i in nums]
    def reset(self) -> [int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.cur = [i for i in self.origin]
        return self.origin

    def shuffle(self) -> [int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.cur[::-1])):
            j = random.randint(0,i)
            self.cur[i],self.cur[j] = self.cur[j],self.cur[i]
        return self.cur
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()