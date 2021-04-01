//
// Created by 郭蕴喆 on 2021/3/31.
//

#ifndef CPPVERSION_123_H
#define CPPVERSION_123_H

#include <vector>
#include <algorithm>

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int firstBuyPrice=INT_MAX;
        int firstSellProfit=INT_MIN;
        int secondBuyPrice=INT_MIN;
        int secondSellProfit=INT_MIN;
        for(int i:prices){
            firstBuyPrice=std::min(firstBuyPrice,i);
            firstSellProfit=std::max(firstSellProfit,i-firstBuyPrice);
            secondBuyPrice=std::max(secondBuyPrice,firstSellProfit-i);
            secondSellProfit=std::max(secondSellProfit,i+secondBuyPrice);
        }
        return secondSellProfit;
    }
};
#endif //CPPVERSION_123_H
