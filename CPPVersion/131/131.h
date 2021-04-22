//
// Created by 郭蕴喆 on 2021/4/17.
//

#ifndef CPPVERSION_131_H
#define CPPVERSION_131_H

#include "../UTILS.h"
class Solution {
    vector<vector<string>> res;
public:

    static bool isPalindrome(int begin, int end,string s){
        while (begin<end){
            if (s[begin]!=s[end]){
                return false;
            }
            begin+=1;
            end-=1;
        }
        return true;
    }

    void DFS(int start, const string& s ,const vector<string>& path){
        if (start>=s.size()){
            this->res.emplace_back(path);
            return;
        }
        for (int step = 0; step < s.size() - start; ++step) {
             if (Solution::isPalindrome(start,start+step,s)){
                 vector<string> temp= path;
                 temp.emplace_back(s.substr(start,step+1));
                 this->DFS(start+step+1,s,temp);
             }
        }
    }
    vector<vector<string>> partition(string s) {
        this->DFS(0,s,vector<string>());
        return this->res;
    }
};
#endif //CPPVERSION_131_H
