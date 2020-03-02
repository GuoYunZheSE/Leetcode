# @Date    : 21:42 03/02/2020
# @Author  : ClassicalPi
# @FileName: LQ.py
# @Software: PyCharm
import re

if __name__ == '__main__':
    S = "Lin Qiao, Guo Yun Zhe"

    # 方法一：不使用内置方法，我们自己来写喔
    left, right = 0, 0
    words1 = []
    while right<len(S):
        if S[right] == ' ':
            words1.append(S[left:right])
            left=right+1
        if right == len(S)-1:
            words1.append(S[left:right+1])
            left=right+1
        if S[right]==',':
            words1.append(S[left:right])
            right+=1
            left=right+1
        right+=1
    print("words1:{}".format(words1))

    #方法二：使用内置split方法

    # ['Lin Qiao', 'Guo Yun Zhe']
    temp=S.split(', ')

    words2=[]
    for each in temp:
        words2+=each.split(' ')
    print("words2:{}".format(words2))

    #方法三：方法二的简化版本
    words3=[]
    words3+=[a.split(' ') for a in S.split(', ')]
    print("words3:{}".format(words3))

    #方法四：使用re包
    words4=re.split(', | ',S)
    print("words4:{}".format(words4))