//
// Created by 郭蕴喆 on 2020/2/27.
//

#ifndef CPPVERSION_862_H
#define CPPVERSION_862_H

#include <iostream>
#include <vector>
#include <deque>
class Solution {
public:
    int shortestSubarray(std::vector<int>& A, int K) {

        std::vector<int> sum(A.size());
        int res=A.size()+1;
        sum[0]=A[0];
        for (int a = 0; a < A.size(); ++a) {
            sum.push_back(sum.back()+A[a]);
        }

        std::deque<int> ascend;
        for (int i = 0; i < sum.size(); ++i) {
            while (!ascend.empty() && sum[i]<sum[ascend.back()]){
                ascend.pop_back();
            }
            while (!ascend.empty() && (sum[i]-sum[ascend.front()])>=K){
                res=std::min(res,i-ascend.front());
                ascend.pop_front();
            }
            ascend.push_back(i);
        }
        if (res==A.size()+1){
            return -1;
        }
        return res;
    }
};
#endif //CPPVERSION_862_H
