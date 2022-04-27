# @Date    : 16:59 04/26/2022
# @Author  : ClassicalPi
# @FileName: 541.py
# @Software: PyCharm
class Solution(object):
    def reverseStr(self, s, k):
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)