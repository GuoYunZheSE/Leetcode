//
// Created by 郭蕴喆 on 2019/12/9.
//

#ifndef CPPVERSION_441_H
#define CPPVERSION_441_H

#endif //CPPVERSION_441_H

#include <cmath>

class Solution {
public:
    int arrangeCoins(int n) {
        if (n==0){
            return 0;
        } else{
            long m=0;
            while (true){
                if ((m+1)*m/2<=n){
                    if (m!=0){
                        m=m*2;
                    } else{
                        m=1;
                    }
                } else{
                    return this->bisearch(int(m/2),m,n)-1;
                }
            }
        }
    }
    int bisearch(int left, int right, int target){
        long mid=round((double(right)+double(left))/2);
        if ((mid+1)*mid/2==target){
            return mid+1;
        }
        if ((mid+1)*mid/2<target){
            return this->bisearch(mid,right,target);
        } else{
            if ((mid-1)*mid/2<=target){
                return mid;
            } else{
                return this->bisearch(left,mid,target);
            }
        }
    }
};