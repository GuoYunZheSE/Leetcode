# @Date    : 20:06 04/28/2021
# @Author  : ClassicalPi
# @FileName: 217.py
# @Software: PyCharm
import collections

def getSize(area:float):
    long=1.0
    res=[]
    while long < area:
        width=area/long
        res.append((long,width))
        long+=0.1
    for each in res:
        print("长：{:.2f} 宽：{:.2f}".format(each[0],each[1]))

def getGrade():
    def combination(base,num):
        denomiator=1
        numerator=1
        while num>0:
            numerator*=base
            denomiator*=num
            num-=1
            base-=1
        return numerator/denomiator
    s=0
    for i in range(0,29):
        s=s+pow(0.8,90-i)*combination(90,i)
    return s/pow(5,90)

class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        d=collections.Counter(nums)
        return any(i>=2 for i in list(d.values()))

if __name__ == '__main__':
    print(getGrade())