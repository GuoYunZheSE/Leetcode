//
// Created by 郭蕴喆 on 2020/6/29.
//

#ifndef CPPVERSION_1491_H
#define CPPVERSION_1491_H

#include <vector>

class Solution {
public:
    double average(std::vector<int>& salary) {
        int minimum=INT_MAX;
        int maximum=INT_MIN;
        int sum=0;
        for (auto iter=salary.begin();iter<salary.end();++iter){
            minimum=std::min(minimum,*iter);
            maximum=std::max(maximum,*iter);
            sum+=*iter;
        }
        return (sum-maximum-minimum)/(double)(salary.size()-2);
    }
};
#endif //CPPVERSION_1491_H
