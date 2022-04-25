# @Date    : 15:07 04/24/2022
# @Author  : ClassicalPi
# @FileName: 524.py
# @Software: PyCharm

import collections
class Solution:
    def leastBricks(self, wall: [[int]]) -> int:
        edges = collections.defaultdict(int)
        for eachrow in wall:
            cur = 0
            for eachbrick in eachrow:
                cur += eachbrick
                edges[cur] += 1
        edges.pop(sum(wall[0]))
        return  len(wall) - (max(edges.values()) if edges else 0)

if __name__ == '__main__':
    S = Solution()
    print(S.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))