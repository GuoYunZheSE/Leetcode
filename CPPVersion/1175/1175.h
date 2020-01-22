//
// Created by 郭蕴喆 on 2020/1/21.
//

#ifndef CPPVERSION_1175_H
#define CPPVERSION_1175_H

#include <cmath>

class Solution {
public:
    int primeNums;
    Solution(){
        this->primeNums=0;
    }
    bool isPrime(int num){
        if (num<=3){
            if (num==2 or num==3){
                return true;
            } else{
                return false;
            }
        } else{
            int root=int(sqrt(num));
            for (int i = 2; i <=root ; ++i) {
                if (num%i==0){
                    return false;
                }
            }
            return true;
        }
    }
    long long int factorail(int num){
        long long int res=1;
        for (int i=num;i>0;--i){
            res*=i;
            res=res%(int(1e9)+7);
        }
        return res;
    }
    int numPrimeArrangements(int n) {
        for (int i = 0; i < n+1; ++i) {
            if (this->isPrime(i)){
                this->primeNums+=1;
            }
        }
        return this->factorail(this->primeNums)*(this->factorail(n-this->primeNums))%(int(1e9)+7);
    }
};
#endif //CPPVERSION_1175_H
