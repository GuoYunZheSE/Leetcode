# @Date    : 23:37 07/31/2020
# @Author  : ClassicalPi
# @FileName: 13.py
# @Software: PyCharm
import collections
class Solution:
    def romanToInt(self, s: str) -> int:
        alphabeta=dict(zip("IVXLCDM",[1,5,10,50,100,500,1000]))
        if len(s)==1:
            return alphabeta[s[0]]

        res=0
        temp=collections.deque([])
        for each in s:
            if len(temp)==2:
                if alphabeta[temp[0]]>=alphabeta[temp[1]]:
                    res+=alphabeta[temp.popleft()]
                else:
                    res-=alphabeta[temp.popleft()]
                    res+=alphabeta[temp.popleft()]
            temp.append(each)
        if temp:
            if len(temp)==2:
                if alphabeta[temp[0]]>=alphabeta[temp[1]]:
                    res+=alphabeta[temp.popleft()]
                    res += alphabeta[temp.popleft()]
                else:
                    res-=alphabeta[temp.popleft()]
                    res+=alphabeta[temp.popleft()]
            else:
                res+=alphabeta[temp.popleft()]
        return res

if __name__ == '__main__':
    S=Solution()
    print(S.romanToInt("III"))
    print(S.romanToInt("IV"))
    print(S.romanToInt("IX"))
    print(S.romanToInt("LVIII"))
    print(S.romanToInt("MCMXCIV"))

