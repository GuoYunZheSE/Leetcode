//
// Created by 郭蕴喆 on 2020/2/24.
//

#ifndef CPPVERSION_1358_H
#define CPPVERSION_1358_H

#include <string>
#include <unordered_map>
class Solution {
public:
    int numberOfSubstrings(std::string s) {
        int left=0,res=0;
        std::unordered_map<char,int> check({{'a',0},{'b',0},{'c',0}});
        for (int right = 0; right < s.size(); ++right) {
            check[s[right]]+=1;
            while (check['a']&&check['b']&&check['c']){
                check[s[left]]-=1;
                left+=1;
            }
            res+=left;
        }
        return res;
    }
};
#endif //CPPVERSION_1358_H
