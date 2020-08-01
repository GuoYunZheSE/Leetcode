# @Date    : 09:38 08/01/2020
# @Author  : ClassicalPi
# @FileName: 1.py
# @Software: PyCharm
import sys
import time
import re
class Solution():
    def aniversaire(self):
        self.dic={}
        lines=[]

        pattern=re.compile(r"([0-9]{2}\-[0-9]{2}\-[0-9]{4})")
        pattern2 = re.compile(r"([0-9]{4}\-[0-9]{2}\-[0-9]{4})")
        line = sys.stdin.readline().strip()
        lines.append(line)
        for line in lines:
            dates=re.findall(pattern,line)
            if dates:
                for date in dates:
                    try:
                        t_st=time.strptime(date,"%d-%m-%Y")
                        if not 2001<=t_st[0]<=2020:
                            continue
                        if not self.dic.__contains__(date):
                            self.dic.setdefault(date,1)
                        else:
                            self.dic[date]+=1
                    except:
                        continue
            dates2=re.findall(pattern2,line)
            if dates2:
                for date in dates2:
                    try:
                        t_st=time.strptime(date[2:],"%d-%m-%Y")
                        if not 2001<=t_st[0]<=2020:
                            continue
                        if not self.dic.__contains__(date[2:]):
                            self.dic.setdefault(date[2:],1)
                        else:
                            self.dic[date[2:]]+=1
                    except:
                        continue
        ani_val=max(list(self.dic.values()))
        for key in list(self.dic.keys()):
            if self.dic[key]==ani_val:
                return key
if __name__ == '__main__':
    S=Solution()
    test="20-12-2030-02-2020-31-2302-02-2012"
    print(S.aniversaire())