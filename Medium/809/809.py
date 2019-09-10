class Solution:
    def expressiveWords(self, S: str, words: [str]) -> int:
        if len(words)==0:
            return 0
        else:
            result=0
            s_groups=self.getGroups(S)
            if len(words)==0:
                return 0
            else:
                for eachword in words:
                    word_groups=self.getGroups(eachword)
                    if len(s_groups)!=len(word_groups):
                        break
                    else:
                        test=0
                        for i in range(0,len(s_groups)):
                            if (s_groups[i][0]==word_groups[i][0] and (len(s_groups[i])==len(word_groups[i]) or (len(s_groups[i])>=3) and len(s_groups[i])>=len(word_groups[i]))):
                                test+=1
                            else:
                                break
                        if test==len(s_groups):
                            result+=1
                return result

    def getGroups(self,words:str)->[[str]]:
        groups=[]
        cursorLeft=0
        while cursorLeft < len(words):
            letter=words[cursorLeft]
            for cursorRight in range(cursorLeft,len(words)):
                letternext=words[cursorRight]
                if letter==letternext:
                    if cursorRight!=len(words)-1:
                        continue
                    else:
                        groups.append(words[cursorLeft:cursorRight+1])
                        cursorLeft = cursorRight+1
                        break
                else:
                    groups.append(words[cursorLeft:cursorRight])
                    cursorLeft=cursorRight
                    break
        return groups

    def getCnt(self, s):
        ans = []
        last = None
        for ch in s:
            if ch == last:
                cnt += 1
            else:
                if last:
                    ans.append((last, cnt))
                cnt = 1
                last = ch
        if last:
            ans.append((last, cnt))
        return ans
if __name__ == '__main__':
    S="HEEELLOOO"
    words=["hello", "hi", "helo"]
    a=Solution()
    print(a.getCnt(S))