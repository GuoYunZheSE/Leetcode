//
// Created by 郭蕴喆 on 2020/2/27.
//

#ifndef CPPVERSION_209_H
#define CPPVERSION_209_H

#include <vector>

class Solution {
public:
    int minSubArrayLen(int s, std::vector<int>& nums) {
        int res=nums.size()+1, cur=0;
        int left=0;
        for (int right = 0; right < nums.size(); ++right) {
            cur+=nums[right];
            while (cur>=s){
                if (cur-nums[left]>=s){
                    cur-=nums[left];
                    left+=1;
                } else{
                    res=std::min(res,right-left+1);
                    break;
                }
            }
        }
        if (res==nums.size()+1){
            return 0;
        }
        return res;
    }
};
#endif //CPPVERSION_209_H
