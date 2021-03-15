# @Date    : 14:09 03/15/2021
# @Author  : ClassicalPi
# @FileName: BitMask.py
# @Software: PyCharm
class Solution:
    def letterCasePermutation(self, S: str) -> [str]:
        res=[]
        location={}
        for index,val in enumerate(S):
            if val.isalpha():
                location[index]=val
        for i in range(2**len(location),2**(len(location)+1)):
            binary=bin(i)[3:]
            temp = [s for s in S]
            for i in range(len(location)):
                if binary[i]=='0':
                    temp[list(location.keys())[i]]=temp[list(location.keys())[i]].lower()
                else:
                    temp[list(location.keys())[i]]=temp[list(location.keys())[i]].lower().upper()
            res.append("".join(temp))
        return res
if __name__ == '__main__':
    S=Solution()
    print(S.letterCasePermutation("a1b2"))