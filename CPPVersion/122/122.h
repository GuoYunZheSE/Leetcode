//
// Created by 郭蕴喆 on 2021/3/31.
//

#ifndef CPPVERSION_122_H
#define CPPVERSION_122_H

#include <vector>
class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int profit=0;
        for (int i = 0; i < prices.size()-1; ++i) {
            if (prices[i+1]>prices[i]){
                profit+=prices[i+1]-prices[i];
            }
        }
        return profit;
    }
};
#endif //CPPVERSION_122_H
