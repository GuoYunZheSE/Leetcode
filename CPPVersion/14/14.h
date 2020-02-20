//
// Created by 郭蕴喆 on 2020/2/21.
//

#ifndef CPPVERSION_14_H
#define CPPVERSION_14_H

#include <string>
#include <vector>

class Solution {
public:
    std::string longestCommonPrefix(std::vector<std::string>& strs) {
        if (strs.empty()){
            return "";
        }
        std::string res="";
        for (int i = 0; i < strs[0].size(); ++i) {
            for (std::string s : strs){
                if (s.size()-1<i || s[i]!=strs[0][i]){
                    return res;
                }
            }
            res.push_back(strs[0][i]);
        }
        return res;
    }
};
#endif //CPPVERSION_14_H
