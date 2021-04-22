# @Date    : 13:52 04/17/2021
# @Author  : ClassicalPi
# @FileName: 171.py
# @Software: PyCharm
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        d={}
        for i in range(1,27):
            d.setdefault(i,s[i-1])

        res=0
        count=0
        for c in columnTitle[::-1]:
            res+=(26**count)*d[c]
            count+=1
        return res