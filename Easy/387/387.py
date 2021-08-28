# @Date    : 16:55 08/14/2021
# @Author  : ClassicalPi
# @FileName: 387.py
# @Software: PyCharm
import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = collections.Counter(s)
        for c in s:
            if dic[c] == 1:
                return s.index(c)
        return -1