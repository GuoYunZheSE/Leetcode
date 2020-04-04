# @Date    : 22:39 04/04/2020
# @Author  : ClassicalPi
# @FileName: 5360.py
# @Software: PyCharm
class Solution:
    def __init__(self):
        self.dic={}
    def countLargestGroup(self, n: int) -> int:
        for i in range(1,n+1):
            s=0
            for j in str(i):
                s+=int(j)
            if self.dic.__contains__(s):
                self.dic[s].append(i)
            else:
                self.dic.setdefault(s,[i])
        fl=[len(a[1]) for a in self.dic.items()]
        return fl.count(max(fl))


if __name__ == '__main__':
    s=Solution()
    print(s.countLargestGroup(15))