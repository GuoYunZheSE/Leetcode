import collections
import copy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):return False
        if not s1 or not s2: return True
        dic=collections.Counter(s1)

        temp = copy.deepcopy(dic)
        Change = False
        i=0
        count=0
        while i<len(s2):
            if s2[i] in temp:
                Change=True
                if temp[s2[i]]==1:
                    temp.pop(s2[i])
                else:
                    temp[s2[i]]-=1
                count+=1
            else:
                if temp=={}:
                    return True
                if Change:
                    temp = copy.deepcopy(dic)
                    i=i-count
                    count=0
                    Change=False
            i+=1
        return temp=={}
if __name__ == '__main__':
    s1="ab"
    s2="eidboaoo"
    s=Solution()
    print(s.checkInclusion(s1,s2))