//
// Created by 郭蕴喆 on 2020/3/14.
//

#ifndef CPPVERSION_1287_H
#define CPPVERSION_1287_H

#endif //CPPVERSION_1287_H

#include <vector>
#include <iostream>
#include <unordered_map>

class Solution {
public:
    int findSpecialInteger(std::vector<int>& arr) {
        std::unordered_map<int,int> dict;
        for(int i:arr){
            if (dict.find(i)!=dict.end()){
                dict[i]+=1;
            } else{
                dict.emplace(i,1);
            }
        }
        std::cout<<dict.size()/4;
        for (std::unordered_map<int,int>::iterator it=dict.begin(); it !=dict.end(); ++it) {
            if(it->second>(arr.size()/4)){
                return it->first;
            }
        }
        return -1;
    }
};