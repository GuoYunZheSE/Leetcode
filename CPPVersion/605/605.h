//
// Created by 郭蕴喆 on 2020/2/4.
//

#ifndef CPPVERSION_605_H
#define CPPVERSION_605_H

#include <vector>

class Solution {
public:
    bool canPlaceFlowers(std::vector<int>& flowerbed, int n) {
        int ans = 0;
        if (n == 0) {
            return true;
        }
        if (flowerbed.size() == 1) {
            return flowerbed[0] == 0 && n == 1;
        }
        for (int i = 0; i < flowerbed.size(); ++i) {
            if (flowerbed[i]==0)
            {
                if (i == 0) {
                    if (flowerbed[i + 1] == 0) {
                        flowerbed[i] = 1;
                        ans += 1;
                    }
                } else if (i == (flowerbed.size() - 1)) {
                    if (flowerbed[i - 1] == 0) {
                        flowerbed[i] = 1;
                        ans += 1;
                    }
                } else{
                    if ((flowerbed[i-1]==0)&&(flowerbed[i+1]==0)){
                        flowerbed[i]=1;
                        ans+=1;
                    }
                }
            }
        }
        return ans>=n;
    }
};
#endif //CPPVERSION_605_H
