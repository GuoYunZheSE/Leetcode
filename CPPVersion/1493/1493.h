
//
// Created by 郭蕴喆 on 2020/6/30.
//

#ifndef CPPVERSION_1493_H
#define CPPVERSION_1493_H

#include <deque>
#include <vector>

class Solution {
public:
    int longestSubarray(std::vector<int>& nums) {
        std::deque<int> window;
        int res=INT_MIN;
        int count_zero=0;
        for (auto iter=nums.begin();iter!=nums.end();++iter){
            window.push_back(*iter);
            if (*iter==0){
                count_zero+=1;
                if (count_zero==2){
                    res=std::max(res,int(window.size()-2));
                }
            }
            while (count_zero>1){
                int temp=window.front();
                window.pop_front();
                if (temp==0){
                    count_zero-=1;
                }
            }
            res=std::max(res,int(window.size()-1));
        }
        return res;
    }
};

#endif //CPPVERSION_1493_H
