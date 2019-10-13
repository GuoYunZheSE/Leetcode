class Solution:
    def numSpecialEquivGroups(self, A: [str]) -> int:
        res={}
        count=0
        while len(A)>0:
            i=0
            str_i=A[0]
            res.setdefault(i + count, [str_i])
            B= A.copy()
            for j,str_j in enumerate(B):
                if len(str_i)==len(str_j) and i!=j:
                    match = True
                    i_list=list(str_i)
                    j_list = list(str_j)
                    for index_i in range(0,len(str_j)):
                        if i_list[index_i]!=j_list[index_i]:
                            find = False
                            for index_j in range(index_i,len(B[j]),2):
                                if i_list[index_i]==j_list[index_j]:
                                    temp=j_list[index_j]
                                    j_list[index_j]=j_list[index_i]
                                    j_list[index_i]=temp
                                    find=True
                                    break
                            if not find:
                                match=False
                                break
                    if match:
                        if res.__contains__(i+count):
                            temp=res[i+count]
                            temp.append(str_j)
                            res.update({i+count:temp})
                        else:
                            res.setdefault(i+count,[str_i])
                        A.remove(str_j)
            count+=1
            print(res)
            print(A)
            A.remove(str_i)
        return len(res)

if __name__ == '__main__':
    A=["aa","bb","ab","ba"]
    S=Solution()
    print(S.numSpecialEquivGroups(A))
