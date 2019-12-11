# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         self.map={}
#         for eachletter in s:
#             if self.map.__contains__(eachletter):
#                 self.map.update({eachletter:self.map.get(eachletter)+1})
#             else:
#                 self.map.setdefault(eachletter,1)
#         even=0
#         odd=0
#         for eachcount in list(self.map.values()):
#             if eachcount%2!=0:
#                 if odd==0:
#                     odd=1
#                 even+=eachcount-1
#             if eachcount%2==0:
#                 even+=eachcount
#         return odd+even

class Solution:
    def longestPalindrome(self, s: str) -> int:
        temp=0
        res=0
        mark=False
        pre=s[0]
        for eachletter in s:
            if eachletter==pre:
                temp+=1
            else:
                pre=eachletter
                if temp%2==0:
                    res+=temp
                else:
                    if not mark:
                        res+=temp
                        mark=True
                    else:
                        res+=temp-1
                temp=1
        if temp % 2 == 0:
            res += temp
        else:
            if not mark:
                res += temp
                mark = True
            else:
                res += temp - 1
        return res
if __name__ == '__main__':
    s= Solution()
    print(s.longestPalindrome("aaaaabbbbccccddd"))