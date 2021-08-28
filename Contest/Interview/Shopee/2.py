# @Date    : 11:19 08/20/2021
# @Author  : ClassicalPi
# @FileName: 2.py
# @Software: PyCharm
# 小于n的整数
# 详细描述
# 输入一个正整数，返回与 n 组成数字完全相同，且小于 n 的最大整数。
import sys
def findMinNumber(s:str):
    if len(s) < 2:
        return 0
    res = (sys.maxsize,"0")
    for end in range(len(s) - 1,-1,-1):
        for begin in range(0,end):
            if int(s[end]) < int(s[begin]):
                diff = (int(s[begin])-int(s[end]))*(10**(len(s)-begin)) + (int(s[begin])-int(s[end]))*(10**(len(s)-end))
                if diff < res[0]:
                    temp = s[0:begin] + s[end] + s[begin+1:end] + s[begin]
                    if end < len(s) - 1:
                        temp += s[end+1:]
                    res = (diff,temp)
    return res[1]

if __name__ == '__main__':
    # n = sys.stdin.readline().strip()
    print(findMinNumber("2332133123213123321321321321312413434"))