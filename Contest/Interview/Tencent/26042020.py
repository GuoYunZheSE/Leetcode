# @Date    : 19:59 04/26/2020
# @Author  : ClassicalPi
# @FileName: 26042020.py
# @Software: PyCharm

# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))
#
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         for v in values:
#             ans += v
#     print(ans)

import sys
class FC():
    def solution(self):
        testcases=int(sys.stdin.readline().strip())
        for i in range(testcases):
            relationships=int(sys.stdin.readline().strip())
            dict={}
            for j in range(relationships):
                line = sys.stdin.readline().strip()
                values = list(map(int, line.split()))
                if dict.__contains__(values[0]):
                    if dict.__contains__(values[1]):
                        dict[values[0]]=dict[values[0]].union(dict[values[1]])
                    else:
                        dict[values[0]].add(values[1])
                else:
                    if dict.__contains__(values[1]):
                        dict.setdefault(values[0],dict[values[1]])
                    else:
                        dict.setdefault(values[0],set())
                        dict[values[0]].add(values[0])
                        dict[values[0]].add(values[1])

                if dict.__contains__(values[1]):
                    if dict.__contains__(values[0]):
                        dict[values[1]]=dict[values[1]].union(dict[values[0]])
                    else:
                        dict[values[1]].add(values[0])
                else:
                    if dict.__contains__(values[0]):
                        dict.setdefault(values[1],dict[values[0]])
                    else:
                        dict.setdefault(values[1],set())
                        dict[values[1]].add(values[0])
                        dict[values[1]].add(values[1])
            print(dict)
            print(max([len(a) for a in list(dict.values())]))
if __name__ == '__main__':
    fc=FC()
    fc.solution()