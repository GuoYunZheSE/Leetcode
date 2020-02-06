//
// Created by 郭蕴喆 on 2020/2/6.
//

#ifndef CPPVERSION_121_H
#define CPPVERSION_121_H

#include <vector>
class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        if (prices.empty()){
            return 0;
        }
        int buyPrice=prices[0];
        int ans=0;
        for(int price:prices){
            ans=std::max(ans,price-buyPrice);
            buyPrice=std::min(buyPrice,price);
        }
        return ans;
    }
};
#endif //CPPVERSION_121_H
