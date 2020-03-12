# @Date    : 12:22 03/12/2020
# @Author  : ClassicalPi
# @FileName: Same.py
# @Software: PyCharm

if __name__ == '__main__':
    length,x=input().split(' ')
    length=int(length)
    x=int(x)
    l=[int(a) for a in input().split(' ')]
    Max=0
    lor=[a|x for a in l]
    for i in l:
        if i|x==i:
            Max=max(Max,lor.count(i))
        else:
            Max = max(Max, l.count(i)+lor.count(i))
    print(Max)