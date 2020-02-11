class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        T=[[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    T[i][j]=T[i-1][j-1]+1
                else:
                    T[i][j]=max(T[i-1][j],T[i][j-1])
        return len(word2)+len(word1)-2*T[len(word1)][len(word2)]

if __name__ == '__main__':
    S=Solution()
    word1="sea"
    word2="eat"
    print(S.minDistance(word1,word2))