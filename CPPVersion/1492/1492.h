//
// Created by 郭蕴喆 on 2020/6/30.
//

#ifndef CPPVERSION_1492_H
#define CPPVERSION_1492_H

class Solution {
public:
    int kthFactor(int n, int k) {
        int count=0;
        for (int i = 0; i < n; ++i) {
            if(n%i==0){
                count+=1;
                if (count==k){
                    return i;
                }
            }
        }
        return -1;
    }
};
#endif //CPPVERSION_1492_H
