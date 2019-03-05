# Class:Easy
# Data:Tuesday, 05/03/2019
# Runtime: 56 ms, faster than 80.93% of Python3 online submissions for Self Dividing Numbers.
# Memory Usage: 13.1 MB, less than 6.29% of Python3 online submissions for Self Dividing Numbers.
class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        SDNs=[]
        for eachnumber in range(left,right+1):
            A=eachnumber.__str__()
            if A.count('0')!=0:
                continue
            else:
                Mark=True
                for each in A:
                    if eachnumber%int(each)!=0:
                        Mark=False
                        break
                if Mark:
                    SDNs.append(eachnumber)
        return SDNs
if __name__ == '__main__':
    s=Solution
    A=s.selfDividingNumbers(s,1,22)
    print(A)