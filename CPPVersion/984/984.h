//
// Created by 郭蕴喆 on 2019/11/19.
//

#ifndef CPPVERSION_984_H
#define CPPVERSION_984_H

#include <string>

using namespace std;

class Solution {
public:
    string strWithout3a3b(int A, int B) {
        string res;
        if (A+B==0){
            return "";
        }
        while (A!=0 and B!=0){
            if (A>B){
                res.append("aab");
                A-=2;
                B-=1;
            } else{
                if (A<B){
                    res.append("bba");
                    A-=1;
                    B-=2;
                } else{
                    res.append("ab");
                    A-=1;
                    B-=1;
                }
            }
        }
        if(A!=0){
            for (int i = 0; i < A; ++i) {
                res.append("a");
            }
        } else{
            if (B!=0){
                for (int i = 0; i <B ; ++i) {
                    res.append("b");
                }
            }
        }
        return res;
    }
    void test(int A,int B);
};
#endif //CPPVERSION_984_H
