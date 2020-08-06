# @Date    : 22:27 08/06/2020
# @Author  : ClassicalPi
# @FileName: LCPN.py
# @Software: PyCharm

class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        Phone={
            '2':'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res=[]
        for d in digits:
            if len(res)==0:
                for each in Phone[d]:
                    res.append(each)
            else:
                temp=[]
                for r in res:
                    for each in Phone[d]:
                        temp.append(r+each)
                res=temp
        return res

if __name__ == '__main__':
    S=Solution()
    print(S.letterCombinations("23"))