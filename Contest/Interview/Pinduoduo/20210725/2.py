# @Date    : 20:39 07/25/2021
# @Author  : ClassicalPi
# @FileName: 2.py
# @Software: PyCharm
import sys
import collections
class Solution:
    def PlatCards(self,Hen:[],Duck:[]):
        tableDic = {}
        tableArrary = collections.deque([])

        Hen = collections.deque(Hen)
        Duck = collections.deque(Duck)

        HenCredit = 0
        DuckCredit = 0

        goDuck, goHen = False, False
        while Hen or Duck:
            if Hen and (goDuck==False):
                henCard= Hen.popleft()
                if tableDic.get(henCard,-1)==-1:
                    tableArrary.append(henCard)
                    tableDic.setdefault(henCard,len(tableArrary)-1)
                    goHen = False
                else:
                    cardIndex = tableDic.get(henCard,-1)
                    HenCredit += henCard
                    for i in range(cardIndex,len(tableArrary)):
                        card = tableArrary.pop()
                        HenCredit += card
                        tableDic.pop(card)
                    goHen = (len(Hen)>0)
                    continue
            if Duck and (goHen==False):
                duckCard = Duck.popleft()
                if tableDic.get(duckCard,-1)==-1:
                    tableArrary.append(duckCard)
                    tableDic.setdefault(duckCard,len(tableArrary)-1)
                    goDuck = False
                else:
                    cardIndex = tableDic.get(duckCard,-1)
                    DuckCredit += duckCard
                    for i in range(cardIndex,len(tableArrary)):
                        card = tableArrary.pop()
                        DuckCredit += card
                        tableDic.pop(card)
                    goDuck = (len(Duck)>0)
                    continue
        for i in range(len(tableArrary)):
            if i%2==0:
                DuckCredit+=tableArrary[i]
            else:
                HenCredit+=tableArrary[i]
        print(f"{HenCredit} {DuckCredit}")
if __name__ == '__main__':
    n = 2
    s = int(sys.stdin.readline().strip())
    lines = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        lines.append(values)
    S=Solution()
    S.PlatCards(lines[0],lines[1])