# @Date    : 22:17 04/24/2022
# @Author  : ClassicalPi
# @FileName: 1129.py
# @Software: PyCharm

import collections
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: [[int]], blueEdges: [[int]]) -> [int]:
        red_matrix, blue_matrix = [[0 for x in range(n)] for i in range(n)], [[0 for x in range(n)] for i in range(n)]
        for edge in redEdges:
            red_matrix[edge[0]][edge[1]] = 1
        for edge in blueEdges:
            blue_matrix[edge[0]][edge[1]]= 1

        def BFS(destination:int):
            queue = collections.deque([(0, 0, 'R'), (0, 0, 'B')])
            visited = {
                "R": collections.defaultdict(int),
                "B": collections.defaultdict(int)
            }
            while queue:
                dist, dest, prev_color = queue.popleft()
                if dest == destination:
                    return dist
                if prev_color == 'R':
                    for eachnode in range(n):
                         if blue_matrix[dest][eachnode] == 1 and not visited["B"][eachnode]:
                            queue.append((dist + 1, eachnode, "B"))
                            visited["B"][eachnode] = 1
                else:
                    for eachnode in range(n):
                        if red_matrix[dest][eachnode] == 1 and not visited["R"][eachnode]:
                            queue.append((dist + 1, eachnode, "R"))
                            visited["R"][eachnode] = 1
            return -1

        res = []
        for i in range(n):
            res.append(BFS(i))

        return res

if __name__ == '__main__':
    S = Solution()
    print(S.shortestAlternatingPaths(3, [[0,1],[1,2]], []))
    print(S.shortestAlternatingPaths(n = 3, redEdges = [[0,1]], blueEdges = [[1,2]]))
    print(S.shortestAlternatingPaths(5, [[0,1],[1,2],[2,3],[3,4]], [[1,2],[2,3],[3,1]]))
    print(S.shortestAlternatingPaths(5, [[2,0],[4,3],[4,4],[3,0],[1,4]],[[2,1],[4,3],[3,1],[3,0],[1,1],[2,0],[0,3],[3,3],[2,3]]))