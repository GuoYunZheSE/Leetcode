# @Date    : 19:53 04/04/2021
# @Author  : ClassicalPi
# @FileName: 20210404_2.py
# @Software: PyCharm
import sys
import collections

class Solution:
    def max_reduce(self,s:[int]):
        q=collections.deque()
        for each in s:
            if not q:
                q.append(each)
            else:
                if each+q[-1]==10:
                    q.pop()
                else:
                    q.append(each)
        return len(q)

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    s=[]
    line = sys.stdin.readline().strip()
    for i in line:
        s.append(int(i))
    S=Solution()
    print(S.max_reduce(s))
    # print(S.max_reduce([2,1,3,7,9,2]))
    # print(S.max_reduce([2, 1, 3, 4, 3, 1,4]))
    # print(S.max_reduce([1, 4, 6, 9, 3, 7]))