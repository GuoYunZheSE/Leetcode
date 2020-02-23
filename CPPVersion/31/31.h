//
// Created by 郭蕴喆 on 2020/2/24.
//

#ifndef CPPVERSION_31_H
#define CPPVERSION_31_H

#include <vector>

class Solution {
public:
    void nextPermutation(std::vector<int>& nums) {
        int before=nums.back();
        int decentIndex=-1;
        for (int i = nums.size()-1; i >=0 ; --i) {
            if (nums[i]<before){
                decentIndex=i;
                break;
            } else{
                before=nums[i];
            }
        }

        if (decentIndex!=-1){
            int minGreaterIndex=nums.size()-1;
            int minGreaterValue=INT8_MAX;
            for (int j = nums.size()-1; j >decentIndex ; --j) {
                if (nums[j]>nums[decentIndex]){
                    if (nums[j]<minGreaterValue){
                        minGreaterIndex=j;
                        minGreaterValue=nums[j];
                    }
                }
            }
            std::swap(nums[minGreaterIndex],nums[decentIndex]);
            std::sort(nums.begin()+decentIndex+1,nums.end());
        } else{
            std::sort(nums.begin(),nums.end());
        }
    }
};
#endif //CPPVERSION_31_H
