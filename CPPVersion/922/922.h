//
// Created by 郭蕴喆 on 2020/1/27.
//

#ifndef CPPVERSION_922_H
#define CPPVERSION_922_H

#include <vector>
class Solution {
public:
    std::vector<int> sortArrayByParityII(std::vector<int>& A) {
        int odd=1;
        int even=0;
        while (even<A.size()-1 && odd<A.size()-1){
            if (A[even]%2==0){
                even+=2;
                continue;
            } else{
                while (A[odd]%2!=0){
                    odd+=2;
                }
                int temp=A[odd];
                A[odd]=A[even];
                A[even]=temp;
                even+=2;
                odd+=2;
            }
        }
        return A;
    }
};
#endif //CPPVERSION_922_H
