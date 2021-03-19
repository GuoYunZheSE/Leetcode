//
// Created by 郭蕴喆 on 2021/3/19.
//

#ifndef CPPVERSION_239_H
#define CPPVERSION_239_H

#include <vector>
#include <deque>
class Solution {
public:
    std::vector<int> maxSlidingWindow(std::vector<int>& nums, int k) {
        std::deque<int> window = std::deque<int>();
        std::vector<int> res;
        for(std::size_t i = 0; i < nums.size(); ++i){
            while (!window.empty() && nums[window.back()]<nums[i]){
                window.pop_back();
            }
            window.push_back(int(i));
            if (int(i)-window.front()+1>k){
                window.pop_front();
            }
            if (int(i)-k+1>=0){
                res.emplace_back(nums[window.front()]);
            }
        }
        return res;
    }
};
#endif //CPPVERSION_239_H
