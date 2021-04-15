# @Date    : 19:14 04/14/2021
# @Author  : ClassicalPi
# @FileName: 149.py
# @Software: PyCharm
import collections
class Solution:
    def maxPoints(self, points: [[int]]) -> int:
        res=[]
        if len(points)==1:
            return 1
        for point_a in points:
            d = collections.defaultdict(int)
            for point_b in points:
                if point_a!=point_b:
                    denomiator=point_a[0]-point_b[0]
                    numerator=point_a[1]-point_b[1]
                    if denomiator==0:
                        d[None]+=1
                    else:
                        k=numerator/denomiator
                        d[k]+=1
            res.append(max(list(d.values())))
            d = collections.defaultdict(int)
        return max(res)+1
if __name__ == '__main__':
    S=Solution()
    print(S.maxPoints([[0,0]]))
