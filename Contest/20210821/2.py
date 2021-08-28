# @Date    : 16:37 08/21/2021
# @Author  : ClassicalPi
# @FileName: 2.py
# @Software: PyCharm
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 返回Sn的第k位字符
# @param n int整型 Sn的n
# @param k int整型 需要返回的字符下标位
# @return char字符型
#
class Solution:
    def findKthBit(self , n , k ):
        letter = {}
        for i in range(0,26):
            letter.setdefault(i+1,chr(ord('a')+i))
        def invert(s:str)->str:
            res = ""
            for c in s:
                res += letter[26 - (ord(c) - ord('a'))]
            return res
        def reverse(s:str)->str:
            return s[::-1]
        S = "a"
        for i in range(2,n+1):
            S = S + letter[i] + reverse(invert(S))
        return S[k-1]

if __name__ == '__main__':
    S = Solution()
    print(S.findKthBit(3,1))