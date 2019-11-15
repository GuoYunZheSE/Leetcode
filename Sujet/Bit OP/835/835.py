# import copy
#
#
# class Solution:
#
#     def largestOverlap(self, A: [[int]], B: [[int]]) -> int:
#         self.A = A
#         self.B = B
#
#         Temp = copy.deepcopy(A)
#         result = []
#         result.append(self.check(A))
#
#         for i in range(0, len(A) - 1):
#             temp = copy.deepcopy(Temp)
#             right = copy.deepcopy(temp)
#             left = copy.deepcopy(temp)
#             for j in range(0, len(A) - 1):
#                 self.slide_left(left)
#                 self.slide_right(right)
#                 result.append(self.check(left))
#                 result.append(self.check(right))
#             Temp=self.slide_up(Temp)
#             result.append(self.check(Temp))
#
#         Temp = copy.deepcopy(A)
#         Temp=self.slide_down(Temp)
#         result.append(self.check(Temp))
#         for j in range(0, len(A) - 2):
#             temp = copy.deepcopy(Temp)
#             right = copy.deepcopy(temp)
#             left = copy.deepcopy(temp)
#             for j in range(0, len(A) - 1):
#                 self.slide_left(left)
#                 self.slide_right(right)
#                 result.append(self.check(left))
#                 result.append(self.check(right))
#             Temp=self.slide_down(Temp)
#             result.append(self.check(Temp))
#         return max(result)
#
#     def check(self, Temp) -> int:
#         count = 0
#         for rowId, row in enumerate(Temp):
#             for columnId, number in enumerate(row):
#                 if number == self.B[rowId][columnId] == 1:
#                     count += 1
#         return count
#
#     def slide_left(self, t: [[int]]):
#         for i in range(0, len(t)):
#             t[i] = t[i][1:]
#             t[i].append(0)
#
#     def slide_right(self, r: [[int]]):
#         for i in range(0, len(r)):
#             r[i].reverse()
#             r[i].append(0)
#             r[i] = r[i][1:]
#             r[i].reverse()
#
#     def slide_up(self, s: [[int]]):
#         s = s[1:]
#         s.append([0 for i in range(0, len(s[0]))])
#         return s
#
#     def slide_down(self, a: [[int]]):
#         a.reverse()
#         a.append([0 for i in range(0, len(a[0]))])
#         a = a[1:]
#         a.reverse()
#         return a
#
#
# if __name__ == '__main__':
#     A=[[1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#      [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
#      [0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
#      [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
#      [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]]
#     B=[[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#      [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
#      [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
#      [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
#      [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
#     S = Solution()
#     print(S.largestOverlap(A, B))
class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        def count_ones(n):
            res = 0
            while n > 0:
                res += 1
                n -= n&(-n)
            return res
        m,n = len(A), len(A[0])
        bin_a = []
        bin_b = []
        for i in range(m):
            temp_a = temp_b = 0
            for j in range(n):
                temp_a = (temp_a<<1) + A[i][j]
                temp_b = (temp_b<<1) + B[i][j]
            bin_a += [temp_a]
            bin_b += [temp_b<<n]
        bin_b = [0]*m+bin_b+[0]*m
        res = 0
        for i in range(2*m):
            for j in range(2*n):
                temp = 0
                for a,b in zip(bin_a, bin_b[i:i+m]):
                    temp += count_ones(a&(b>>j))
                res = max(res,temp)
        return res