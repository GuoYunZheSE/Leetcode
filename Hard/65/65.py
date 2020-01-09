class Solution:
    def containPoint(self,s:str)->int:
        count=0
        for each in s:
            if each=='.':
                count+=1
        return count
    def containNumber(self,s:str)->int:
        count=0
        for each in s:
            if each.isdigit():
                count+=1
        return count
    def containLetter(self,s:str)->[]:
        count=0
        findE=False
        for each in s:
            if ord(each)>=65 and ord(each)<=122:
                count+=1
                if each=='e':
                    findE=True
        return [count,findE]

    def containSign(self,s:str)->int:
        count=0
        for each in s:
            if  each=='+' or each=='-':
                count+=1
        return count

    def isNumber(self, s: str) -> bool:
        s=s.strip(' ')
        if s=='' or s=='.':
            return False
        for each in s:
            if each==' ':
                return False
        letterCount,findE=self.containLetter(s)
        if letterCount>=2 or (letterCount==1 and not findE):
            return False
        else:
            if findE:
                base,exponent=s.split('e')
                if base=='' or exponent=='':
                    return False
                else:
                    baseSign=self.containSign(base)
                    expSign=self.containSign(exponent)
                    if baseSign>=2 or expSign>=2:
                        return False
                    else:
                        if baseSign==1 and (not (base[0]=='+' or base[0]=='-') or len(base)==1):
                            return False
                        if expSign==1 and (not (exponent[0]=='+' or exponent[0]=='-') or len(exponent)==1):
                            return False
                        if self.containPoint(base)>1 or self.containPoint(exponent)>0:
                            return False
                        if not self.containNumber(base) or not self.containNumber(exponent):
                            return False
                        else:
                            if len(base)==1 and base[0]=='.':
                                return False
                            return True
            else:
                countSign=self.containSign(s)
                if not self.containNumber(s):
                    return False
                if countSign>=2:
                    return False
                else:
                    if countSign==1 and (not (s[0]=='+' or s[0]=='-') or len(s)==1):
                        return False
                    else:
                        if self.containPoint(s)>1:
                            return False
                        else:
                            return True

if __name__ == '__main__':
    S="  -90e3  "
    sol=Solution()
    sol.isNumber(S)