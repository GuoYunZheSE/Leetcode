# @Date    : 19:07 07/25/2021
# @Author  : ClassicalPi
# @FileName: 1.py
# @Software: PyCharm
import collections
import sys
class Solution:
    def LineCheck(self,lines:[[]]):
        self.dic = collections.defaultdict(set)
        for lineID,lineContent in enumerate(lines):
            for index in range(lineContent[0],lineContent[1]+1):
                self.dic[index].add(lineID)
        for lineID,lineContent in enumerate(lines):
            if len(self.dic[lineContent[0]].intersection(self.dic[lineContent[1]]))>1:
                return True
        return False

if __name__ == '__main__':
    S=Solution()
    n = int(sys.stdin.readline().strip())
    lines = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        lines.append(values)
    if S.LineCheck(lines):
        print("true")
    else:
        print("false")
    # print(S.LineCheck([[2,3],[1,9],[4,10],[5,20]]))
    # print(S.LineCheck([[1, 3], [4, 5], [7, 10], [13, 18]]))