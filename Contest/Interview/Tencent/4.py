# @Date    : 21:44 04/26/2020
# @Author  : ClassicalPi
# @FileName: 4.py
# @Software: PyCharm
import sys
class Perfect_Pair():
    def check(self,l1,l2):
        l3=[l1[a]+l2[a] for a in range(len(l1))]
        for each in l3:
            if each!=l3[0]:
                return False
        return True
    def solution(self):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        item_num,attr_num=values[0],values[1]
        data=[]
        for i in range(item_num):
            line2 = sys.stdin.readline().strip()
            values2 = list(map(int, line2.split()))
            temp=[]
            for each in values2:
                temp.append(each)
            data.append(temp)
        res=0
        for i in range(0,len(data)-1):
            for j in range(i+1,len(data)):
                if self.check(data[i],data[j]):
                    res+=1
        print(res)
if __name__ == '__main__':
    pp=Perfect_Pair()
    pp.solution()