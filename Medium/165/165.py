class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1=version1.split('.')
        version2=version2.split('.')
        if int(version1[0])>int(version2[0]):
            return 1
        elif int(version1[0])<int(version2[0]):
            return -1
        else:
            number1=''+str(int(version1[0]))
            number2=''+str(int(version2[0]))
            mark1=0
            mark2=0

            if len(version1)>=2:
                for n in range(1,len(version1)):
                    temp=str(int(version1[n]))
                    number1+=temp
                    if int(version1[n])!=0:
                        mark1=0
                    if len(temp)>=2:
                        for m in range(-1,-1-len(temp),-1):
                            if temp[m]=='0':
                                mark1+=1
                            else:break

            if len(version2)>=2:
                for n in range(1,len(version2)):
                    temp=str(int(version2[n]))
                    number2+=temp
                    if int(version2[n])!=0:
                        mark2=0
                    if len(temp)>=2:
                        for m in range(-1,-1-len(temp),-1):
                            if temp[m]=='0':
                                mark2+=1
                            else:break

            factor1=len(number2)
            factor2=len(number1)
            number1=pow(10,factor1+mark1)*int(number1)
            number2=pow(10,factor2+mark2)*int(number2)

            if number1==number2:
                return 0
            elif number1>number2:
                return 1
            else:
                return -1

if __name__ == '__main__':
    version1 = "1.9.9.9"
    version2 = "1.10.0.0"
    S=Solution()
    print(S.compareVersion(version1,version2))