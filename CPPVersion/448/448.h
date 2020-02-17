//
// Created by 郭蕴喆 on 2020/2/17.
//

#ifndef CPPVERSION_448_H
#define CPPVERSION_448_H

#include <vector>

class Solution {
public:
    std::vector<int> findDisappearedNumbers(std::vector<int>& nums) {
        std::vector<bool> b(nums.size(), false);
        std::vector<int> res;
        for (int i=0;i<b.size();++i){
            b[i-1]= true;
        }
        for (int i=0;i<b.size();++i){
            if (!b[i]){
                res.push_back(i+1);
            }
        }
        return res;
    }
};
#endif //CPPVERSION_448_H
