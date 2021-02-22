# @Date    : 18:09 02/22/2021
# @Author  : ClassicalPi
# @FileName: 69.py
# @Software: PyCharm
class Solution:
    def mySqrt(self, x: int) -> int:
        root=x
        while root**2>x:
            root=(root+x/root)//2
        return root