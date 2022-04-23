# @Date    : 22:43 04/23/2022
# @Author  : ClassicalPi
# @FileName: 899.py
# @Software: PyCharm
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min([s[i:] + s[:i] for i in range(len(s))])
        else:
            return "".join(sorted(s))