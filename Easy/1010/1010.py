class Solution:
    def numPairsDivisibleBy60(self, time: [int]) -> int:
        res=0
        used=set()
        if len(time)==0:
            return 0
        dic={}
        for each in time:
            m=each%60
            if dic.__contains__(m):
                temp=dic.get(m)
                temp.append(m)
                dic.update({m:temp})
            else:
                dic.setdefault(m,[each])
        for eachkey in sorted(dic.keys()):
            if eachkey==0 or eachkey==30:
                res+=len(dic.get(eachkey))*(len(dic.get(eachkey))-1)/2
            else:
                if dic.__contains__(60-eachkey) and (60-eachkey)>eachkey:
                    used.add(eachkey)
                    res+=len(dic.get(eachkey))*(len(dic.get(60-eachkey)))
        return int(res)

if __name__ == '__main__':
    time=[60,60,60]
    S=Solution()
    print(S.numPairsDivisibleBy60(time))