# @Date    : 10:35 09/27/2020
# @Author  : ClassicalPi
# @FileName: 5523.py
# @Software: PyCharm

class Solution:
    def minOperations(self, logs: [str]) -> int:
        depth=0
        for log in logs:
            if log=="../":
                if depth>0:
                    depth-=1
                continue
            if log=="./":
                continue
            else:
                depth+=1
        return depth

if __name__ == '__main__':
    S=Solution()
    print(S.minOperations(["d1/","d2/","../","d21/","./"]))