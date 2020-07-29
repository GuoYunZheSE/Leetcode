//
// Created by 郭蕴喆 on 2020/7/29.
//

#ifndef CPPVERSION_11_H
#define CPPVERSION_11_H

#endif //CPPVERSION_11_H

#include <vector>

class Solution {
public:
    int maxArea(std::vector<int>& height) {
        int res=0;
        for (int i = 0; i < height.size(); ++i) {
            for (int j = i; j < height.size(); ++j) {
                res=std::max(res,std::min(height[i],height[j])*(j-i));
            }
        }
        return res;
    }
};