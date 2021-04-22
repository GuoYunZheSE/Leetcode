# @Date    : 14:11 04/17/2021
# @Author  : ClassicalPi
# @FileName: 172.py.py
# @Software: PyCharm
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n<5:
            return 0
        else:
            return n//5+self.trailingZeroes(n//5)