# @Date    : 20:11 07/25/2021
# @Author  : ClassicalPi
# @FileName: 4.py
# @Software: PyCharm
import sys
import collections
class Solution:
    # 99999 22 1
    def MultiProblem(self,nums:[]):
        num1 = ""
        num2 = ""
        all = ""
        for i in range(9,-1,-1):
            for j in range(0,(nums[i])):
                all += f"{i}"
        for i in range(0,len(all)):
            if i % 2 ==0:
                num1+=all[i]
            else:
                num2+=all[i]
        return int(num1)*int(num2)
if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    S=Solution()
    print(S.MultiProblem(values))