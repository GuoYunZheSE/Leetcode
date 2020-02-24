//
// Created by 郭蕴喆 on 2020/2/24.
//

#ifndef CPPVERSION_1356_H
#define CPPVERSION_1356_H

#include <vector>
#include <bitset>
class Solution {
public:
    std::vector<int> sortByBits(std::vector<int>& arr) {
        std::sort(arr.begin(),arr.end(),[](const int & a,const int & b){
            std::bitset<16> x(a),y(b);
            if (x.count()<y.count()){
                return true;
            } else return (x.count()==y.count() && a < b);
        });
        return arr;
    }
};
#endif //CPPVERSION_1356_H
