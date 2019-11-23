//
// Created by 郭蕴喆 on 2019/11/22.
//

#ifndef CPPVERSION_962_H
#define CPPVERSION_962_H

#endif //CPPVERSION_962_H

#include <iostream>
#include <vector>
#include <stack>
#include <cmath>


using namespace std;

class Solution {
public:
    int maxWidthRamp(vector<int>& A);
};

int Solution::maxWidthRamp(vector<int> &A) {
    stack<int> s;
    int res=0;
    for (int i = 0; i < A.size(); ++i) {
        if (s.empty()||A[i]<A[s.top()]){
            s.push(i);
        }
    }
    for (int j = A.size()-1; j >=0 ; --j) {
        while (!s.empty()&&A[j]>=A[s.top()]){
            res=max(res,j-s.top());
            s.pop();
        }
    }
    return res;
}
