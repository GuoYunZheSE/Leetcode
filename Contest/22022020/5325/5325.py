# class Solution:
#     def check(self,state:{}):
#         if (state['a']>=1 and state['b']>=1 and state['c']>=1):
#             return 1
#         else:
#             return 0
#     def numberOfSubstrings(self, s: str) -> int:
#         res=0
#         for i in range(0,len(s)):
#             curr="{}".format(s[i])
#             state = {
#                 'a': 0,
#                 'b': 0,
#                 'c': 0
#             }
#             state[s[i]]+=1
#             for j in range(i+1,len(s)):
#                 curr+=s[j]
#                 state[s[j]]+=1
#                 status=self.check(state)
#                 if status==0:
#                     continue
#                 elif status==1:
#                     res+=1
#                     continue
#         return res
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        table=[]
        res=0
        for i in range(0,len(s)):
            if i==0:
                if s[i]=='a':
                    table.append([1,0,0])
                if s[i]=='b':
                    table.append([0,1,0])
                if s[i] == 'c':
                    table.append([0,0,1])
            else:
                temp = table[-1].copy()
                if s[i]=='a':
                    temp[0]+=1
                if s[i]=='b':
                    temp[1]+=1
                if s[i] == 'c':
                    temp[2]+=1
                if temp[0]>=1 and temp[1]>=1 and temp[2]>=1:
                    res+=1
                table.append(temp)
        for each in s:
            # table.pop(0)
            index=2
            if each=='a':
                index=0
            if each=='b':
                index=1
            for i in range(0,len(table)):
                table[i][index]-=1
                if table[i][0]>=1 and table[i][1]>=1 and table[i][2]>=1:
                    res+=len(table)-i
                    break

        return res



if __name__ == '__main__':
    s = "abcabc"
    s1=Solution()
    print(s1.numberOfSubstrings(s))