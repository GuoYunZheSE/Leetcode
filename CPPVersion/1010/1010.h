//
// Created by 郭蕴喆 on 2020/1/29.
//

#ifndef CPPVERSION_1010_H
#define CPPVERSION_1010_H

#include <vector>
#include <unordered_map>
class Solution {
public:
    int numPairsDivisibleBy60(std::vector<int>& time) {
        int res=0;
        if (time.empty()){
            return 0;
        }
        std::unordered_map<int,std::vector<int>> dic;
        for (int each : time){
            if (dic.find(each%60)==dic.end()){
                dic.insert({each%60,std::vector<int>({each})});
            } else{
                dic[each%60].push_back(each%60);
            }
        }
        for (int i = 0; i < 60; ++i) {
            if(dic.find(i)!=dic.end()){
                if (i==0 || i==30){
                    res+=(dic[i].size()*(dic[i].size()-1))/2;
                } else{
                    if (dic.find(60-i)!=dic.end() && (60-i)>i){
                        res+=(dic[i].size())*(dic[60-i].size());
                    }
                }
            }
        }
        return int(res);
    }
};
#endif //CPPVERSION_1010_H
