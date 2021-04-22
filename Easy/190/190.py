# @Date    : 14:18 04/17/2021
# @Author  : ClassicalPi
# @FileName: 190.py
# @Software: PyCharm
class Solution:
    def __init__(self):
        self.table={0:1}
        for i in range(1,32):
            self.table.setdefault(i,self.table[i-1]*2)
    def reverseBits(self, n: int) -> int:
        s=bin(n)[2:]
        while len(s)<32:
            s="0"+s
        res=0
        for i in range(0,len(s)):
            if s[i]=="1":
                res+=self.table[i]
        return res
if __name__ == '__main__':
    S=Solution()
    print(S.reverseBits(4294967293))