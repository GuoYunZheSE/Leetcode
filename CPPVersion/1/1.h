//
// Created by 郭蕴喆 on 2020/1/29.
//

#ifndef CPPVERSION_1_H
#define CPPVERSION_1_H

#include <vector>
#include <unordered_map>

class Solution {
public:
    std::unordered_map<int,int> dic;
    std::unordered_map<int,int> duplicate;
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        for (int i = 0; i <nums.size() ; ++i) {
            if(this->dic.find(nums[i])==this->dic.end()){
                this->dic.insert({nums[i],i});
            } else{
                this->duplicate.insert({nums[i],i});
            }
        }
        for(int i : nums){
            int remain=target-i;
            if(this->dic.find(remain)!=this->dic.end()){
                if(remain==i){
                    if(this->duplicate.find(remain)!=this->duplicate.end()){
                        return std::vector<int> ({this->dic[i],this->duplicate[remain]});
                    }
                } else{
                    return std::vector<int> ({this->dic[i],this->dic[remain]});
                }
            }
        }
        return std::vector<int> ({-1,-1});
    }
};
#endif //CPPVERSION_1_H
