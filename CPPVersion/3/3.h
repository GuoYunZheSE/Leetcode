//
// Created by 郭蕴喆 on 2020/2/10.
//

#ifndef CPPVERSION_3_H
#define CPPVERSION_3_H

#include <string>
#include <set>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        int res=0;
        std::set<int> cur;
        int i=0;
        int j=0;
        while (j<s.size()){
            if(cur.find(s[j])==cur.end()){
                cur.insert(s[j]);
                j+=1;
            } else{
                res=std::max(res,int(cur.size()));
                cur.erase(s[i]);
                i+=1;
            }
        }
        res=std::max(res,int(cur.size()));
        return res;
    }
};
#endif //CPPVERSION_3_H
