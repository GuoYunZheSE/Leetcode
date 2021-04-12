//
// Created by 郭蕴喆 on 2021/4/12.
//

#ifndef CPPVERSION_127_H
#define CPPVERSION_127_H
#include "../UTILS.h"
class Solution {
public:
    unordered_set<string> wordSet;

    int ladderLength(std::string beginWord, std::string endWord, std::vector<std::string>& wordList) {
        for (string s:wordList){
            this->wordSet.emplace(s);
        }
        if (wordSet.find(endWord)==wordSet.end()){
            return 0;
        }
        vector<std::string> layer({beginWord});
        vector<std::string> nextLayer;
        int res=1;
        unordered_set<string> s({endWord});
        while (!layer.empty()){
            for (const string& now : layer){
                for (int i=0;i<now.size();++i){
                    for (char c : "abcdefghijklmnopqrstuvwxyz"){
                        string temp= now.substr(0,i)+c+now.substr(i+1,now.size());
                        if (temp==endWord){
                            return res+1;
                        }
                        if (wordSet.count(temp)!=0 && s.count(temp)==0){
                            s.emplace(temp);
                            nextLayer.emplace_back(temp);
                        }
                    }
                }
            }
            layer=nextLayer;
            nextLayer=vector<std::string>();
            res+=1;
            for (const string& now : layer){
                s.insert(now);
            }
        }
        return 0;
    }
};
#endif //CPPVERSION_127_H
