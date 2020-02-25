//
// Created by 郭蕴喆 on 2020/2/25.
//

#ifndef CPPVERSION_996_H
#define CPPVERSION_996_H

#include <vector>
#include <cmath>
#include <set>
class Solution {
public:
    bool check(int pre,int num){
        int _sqrt=std::sqrt(pre+num);
        return std::pow(_sqrt, 2) == double(pre + num);
    }
    void DFS(std::vector<std::vector<int>>& res,const std::vector<int>& nums,const std::vector<int>& pre){
        if (nums.empty()){
            res.push_back(pre);
            return;
        } else{
            std::set<int> used;
            for (int i = 0; i < nums.size(); ++i) {
                if (used.find(nums[i])==used.end()){
                    if (pre.empty() || check(pre.back(),nums[i])){
                        used.insert(nums[i]);

                        std::vector<int> temp(nums);
                        temp.erase(temp.begin()+i);
                        std::vector<int> temp2(pre);
                        temp2.push_back(nums[i]);

                        this->DFS(res,temp,temp2);
                    }
                }
            }
            return;
        }
    }
    int numSquarefulPerms(std::vector<int>& nums) {
        std::vector<std::vector<int>> res;
        this->DFS(res,nums,std::vector<int>({}));
        return res.size();
    }
};
#endif //CPPVERSION_996_H
