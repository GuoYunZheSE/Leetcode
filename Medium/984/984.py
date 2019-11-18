class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        res=''
        Bigger={}
        Smaller={}


        if A>B:
            Bigger={'a':A}
            Smaller={'b':B}
        else:
            Bigger={'b':B}
            Smaller={'a':A}

        BigLetter=list(Bigger.keys())[0]
        BigCount=Bigger.get(BigLetter)
        SmallLetter=list(Smaller.keys())[0]
        SmallCount=Smaller.get(SmallLetter)

        if BigCount==1:
            if SmallCount==1:
                return 'ab'
            else:
                return BigLetter

        while BigCount>SmallCount and SmallCount!=0:
            res+='{}{}{}'.format(BigLetter,BigLetter,SmallLetter)
            BigCount-=2
            SmallCount-=1

        # BigCount=SmallCount
        # SmallCount=0

        if BigCount==SmallCount:
            if BigCount!=0:
                for i in range(0,BigCount):
                    res+="{}{}".format(BigLetter,SmallLetter)
                return res
            else:
                return res
        else:
            if BigCount==2:
                return res+BigLetter+BigLetter
            else:
                return res + BigLetter
if __name__ == '__main__':
    S=Solution()
    print(S.strWithout3a3b(32,60))