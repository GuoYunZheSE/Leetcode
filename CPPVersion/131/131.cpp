#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;
int lcp[5001][5001];
ll dp[5001][5001];

using namespace std;
const long long Mod=1e9+7;
long long n,dp[5005][5005],sum[5005][5005];
class Solution {
public:
    int numberOfCombinations(string num) {
        string x = num;
        n = num.size();
        for(int i=n;i>=1;--i){
            for(int j=n;j>i;--j){
                if(x[i]==x[j])
                    lcp[i][j]=lcp[i+1][j+1]+1;
            }
        }
        for(int i=1;i<=n;++i)
            dp[0][i]=1;
        for(int i=1;i<=n;++i){             //这个子串的结尾位置
            int w=i;
            for(int j=1;j<=i;++j){         //dp[i][j]:以【从x[i]往前j长度的子串】结尾的方法数
                int p=i-j+1;               //这个子串的开头位置
                if(x[p]!='0')
                    w=p;                   //这个子串的【非0】开头位置
                int  h=p-1;
                for(int k=p-1;k>=0;--k){   //枚举上一个子串的开头位置(上一个一定不能比这个长，错！比如0012,001比2长但比2小)
                    if(x[k]!='0')
                        h=k;               //这个子串的【非0】开头位置
                    char a=x[h+lcp[h][w]],b=x[w+lcp[h][w]];
                    if(p-h<i-w+1||(p-h==i-w+1&&lcp[h][w]<j&&a<b)) //【这个串较长】或【一样长比较公共序列后第一个不同字符】
                        dp[i][j]=(dp[i][j]+dp[p-1][p-k])%mod;
                }
            }
        }
        ll s=0;
        for(int i=1;i<=n;++i){
            s=(s+dp[n][i])%mod;
        }
        return s;
    }
};