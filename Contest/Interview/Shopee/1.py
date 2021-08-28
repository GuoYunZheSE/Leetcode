# @Date    : 10:56 08/20/2021
# @Author  : ClassicalPi
# @FileName: 1.py
# @Software: PyCharm
# 十六进制回文数
# 详细描述
# 输入一个正整数，判断它的十六进制形式是否为回文数。

import sys
def getHex(n:int):
    next = n
    res = ""
    while next > 0:
        reminder = next % 16
        next = next // 16
        if reminder > 9:
            res += f"{chr(65+reminder-10)}"
        elif reminder > 0:
            res += f"{reminder}"
    return res[::-1]

def check(s:str):
    if len(s) < 2:
        return True
    begin = 0
    end = len(s) - 1
    while begin < end:
        if s[begin] == s[end]:
            begin += 1
            end -= 1
        else:
            return False
    return True

if __name__ == '__main__':
    n = sys.stdin.readline()
    if check(getHex(int(n))):
        print(1)
    else:
        print(0)