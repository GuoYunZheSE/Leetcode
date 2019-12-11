import typing


class Solution:
    def sortArrayByParity(self, A: typing.List[int]) -> typing.List[int]:
        # even=[]
        # odd=[]
        # for each in A:
        #     if each%2==0:
        #         even.append(each)
        #     else:
        #         odd.append(each)
        # return even+odd
        return [a for a in A if a%2==0]+[a for a in A if a%2!=0]
# Runtime: 76 ms, faster than 98.18% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 13.3 MB, less than 98.70% of Python3 online submissions for Sort Array By Parity.
if __name__ == '__main__':
    S=Solution()
    print(S.sortArrayByParity([3,1,2,4]))