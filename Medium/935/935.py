# @Date    : 15:23 08/08/2021
# @Author  : ClassicalPi
# @FileName: 935.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        self.neighborsMap = {
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (3, 9, 0),
            5: tuple(),  # 5 has no neighbors
            6: (1, 7, 0),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4),
            0: (4, 6),
        }
    def neighbors(self,position:int):
        return self.neighborsMap[position]
    def knightDialerMemoRecur(self, n: int, hop:int) -> int:
        if hop ==0 :
            return 1
        else:
            sum = 0
            for neighbor in self.neighbors(n):
                sum += self.knightDialerMemoRecur(neighbor,hop-1)
            return sum
    def knightDialerCachedRecur(self,n,hop)->int:
        cache = {}
        def helper(n,hop):
            if hop == 0:
                return 1
            else:
                sum = 0
                for neighbor in self.neighbors(n):
                    if cache.get((neighbor,hop-1),-1) != -1:
                        sum += cache.get((neighbor,hop-1),-1)
                    else:
                        temp = helper(neighbor,hop-1)
                        sum += temp
                        cache.setdefault((neighbor,hop-1),temp)
                return sum
        return helper(n,hop)

    # def knightDialerDP(self, n, hop) -> int:

if __name__ == '__main__':
    S =Solution()
    print(S.knightDialerCachedRecur(6,900))