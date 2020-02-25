//
// Created by 郭蕴喆 on 2020/2/25.
//

#ifndef CPPVERSION_47_H
#define CPPVERSION_47_H

#include <vector>
#include <set>
class Solution {
public:
    void DFS(std::vector<std::vector<int>>& res,const std::vector<int>& nums,const std::vector<int>& pre){
        if (nums.empty()){
            res.push_back(pre);
            return;
        } else{
            std::set<int> used;
            for (int i = 0; i < nums.size(); ++i) {
                if (used.find(nums[i])==used.end()){
                    used.insert(nums[i]);

                    std::vector<int> temp(nums);
                    temp.erase(temp.begin()+i);
                    std::vector<int> temp2(pre);
                    temp2.push_back(nums[i]);

                    this->DFS(res,temp,temp2);
                }
            }
            return;
        }
    }
    std::vector<std::vector<int>> permuteUnique(std::vector<int>& nums) {
        std::vector<std::vector<int>> res;
        this->DFS(res,nums,std::vector<int>({}));
        return res;
    }
};
#endif //CPPVERSION_47_H
