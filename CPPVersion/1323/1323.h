//
// Created by 郭蕴喆 on 2020/1/23.
//

#ifndef CPPVERSION_1323_H
#define CPPVERSION_1323_H

#include <math.h>

class Solution {
public:
    int maximum69Number (int num) {
        int temp=num;
        int count=0;
        int maxPosition=-1;
        while (num>=1){
            if (num%10==6){
                maxPosition=count;
            }
            count+=1;
            num=int(num/10);
        }
        if (maxPosition==-1){
            return temp;
        } else{
            return 3*pow(10,maxPosition)+temp;
        }

    }
};
#endif //CPPVERSION_1323_H
