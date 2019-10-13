class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_curr=0
        name_length=0

        typed_curr=0
        typed_length=0

        while name_curr<len(name):
            for i in range(name_curr,len(name)):
                if name[i]==name[name_curr]:
                    name_length+=1
                if name[i] != name[name_curr] or i==len(name)-1:
                    if typed[typed_curr] != name[name_curr]:
                        return False
                    for j in range(typed_curr,len(typed)):
                        if typed[j]==typed[typed_curr]:
                            typed_length+=1
                        if typed[j] != typed[typed_curr] or j==len(typed)-1:
                            if typed_length<name_length:
                                return False
                            else:
                                if i==len(name)-1 and j==len(typed)-1 and name[i]!=typed[j]:
                                    return False
                                if i==len(name)-1 and j==len(typed)-1 and name[i]==typed[j]:
                                    return True
                                typed_length=0
                                name_length=0
                                name_curr=i
                                typed_curr=j
                                break
                    break
        return True
    #`
    # class Solution:
    #     def isLongPressedName(self, name: str, typed: str) -> bool:
    #         n1, n2 = len(name), len(typed)
    #         if n1 == n2 == 0:
    #             return True
    #         if n1 == 0 or n2 == 0 or name[0] != typed[0] or name[-1] != typed[-1]:
    #             return False
    #         i, cur = 0, name[0]
    #         for l in typed:
    #             if l == name[i]:
    #                 cur = name[i]
    #                 if i < n1 - 1:
    #                     i += 1
    #             elif cur != l:
    #                 return False
    #         return True`
if __name__ == '__main__':
    S=Solution()
    name = "leelee"
    typed = "lleeelee"
    print(S.isLongPressedName(name,typed))

