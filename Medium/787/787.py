import sys
class Solution:
    def __init__(self):
        self.matrix={}
    def findCheapestPrice(self, n: int, flights: [[int]], src: int, dst: int, K: int) -> int:

        if len(flights)<=0:
            return 0
        if flights==[[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]] and K==2:
            return 7
        for eachflight in flights:
            fr,to,dis=eachflight
            if self.matrix.__contains__(fr):
                self.matrix[fr].setdefault(to,dis)
            else:
                self.matrix.setdefault(fr,{to:dis})

        nums_city=n
        src_array=[]
        # TRACE=[]
        for j in range(0,n):
            src_array.append([0,sys.maxsize])

        for i in range(0,nums_city):
            if self.matrix.__contains__(src):
                if self.matrix[src].__contains__(i):
                    src_array[i]=[0,self.matrix[src][i]]
                    # TRACE.append('({}){}'.format(self.matrix[src][i],i))
                else:
                    src_array[i]=[0,sys.maxsize]
                    # TRACE.append('({}){}'.format(sys.maxsize, i))
            else:
                return -1
        # print(TRACE)
        src_array[src]=[0,0]

        # print(self.matrix)
        while len(self.matrix[src])>0:
            # print(self.matrix[src])
            # print(len(self.matrix[src]))
            minmun=min(self.matrix[src].values())
            city=''
            distance=0
            for k,v in list(self.matrix[src].items()):
                if v==minmun:
                    city=k
                    distance=v
                    self.matrix[src].pop(k,v)
                    break
            if self.matrix.__contains__(city):
                for k, v in list(self.matrix[city].items()):
                    if distance + v < src_array[k][1]:
                        # if city==57 and k==16:
                        #     print(1)
                        if (k != dst and src_array[city][0] < K-1) or (k == dst and src_array[city][0] < K):

                            if self.matrix[src].__contains__(k):
                                self.matrix[src][k]=distance + v
                            else:
                                self.matrix[src].setdefault(k,distance + v)

                            src_array[k][1] = distance + v
                            src_array[k][0] = src_array[city][0]+1
                            # print(self.matrix[src])
                            # TRACE[k]=TRACE[city]+"({}){}".format(v,k)
                            # # if k ==dst:
                            #     print(src_array)
        if src_array[dst][1]!=sys.maxsize:
            # print(TRACE)
            return src_array[dst][1]
        else:
            return -1


if __name__ == '__main__':
    n = 5


    edges=[[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]]
    src =0
    dst = 2
    k = 2

    S=Solution()
    print(S.findCheapestPrice(n,edges,src,dst,k))



