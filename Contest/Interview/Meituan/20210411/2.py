# @Date    : 10:30 04/11/2021
# @Author  : ClassicalPi
# @FileName: 2.py
# @Software: PyCharm
import sys
class Solution:
    def cheatRow(self,M:list,T:list):
        def binarySearch(arr, l, r, x):
            if r >= l:
                mid = int(l + (r - l) / 2)
                if arr[mid] == x:
                    return mid
                elif arr[mid] > x:
                    return binarySearch(arr, l, mid - 1, x)
                else:
                    return binarySearch(arr, mid + 1, r, x)
            else:
                return l
        M=sorted(M)
        T=sorted(T)
        res=-sys.maxsize
        for i in range(0,1001):
            m=binarySearch(M,0,len(M)-1,i)
            t = binarySearch(T, 0, len(T)-1, i)
            res=max(
                res,
                ((len(T)-t-1)*2+t+1)-((len(M)-m-1)*2+m+1)
            )
        return res
if __name__ == '__main__':
    n,k = sys.stdin.readline().strip().split(" ")
    n,k=int(n),int(k)
    line = sys.stdin.readline().strip()
    M = list(map(int, line.split(" ")))
    line = sys.stdin.readline().strip()
    T = list(map(int, line.split(" ")))

    S = Solution()
    print(S.cheatRow(M,T))