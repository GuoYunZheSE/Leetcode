# @Date    : 17:16 04/26/2022
# @Author  : ClassicalPi
# @FileName: 557.py
# @Software: PyCharm
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([x[::-1] for x in s.split(" ")])