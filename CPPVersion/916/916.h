//
// Created by 郭蕴喆 on 2020/2/27.
//

#ifndef CPPVERSION_916_H
#define CPPVERSION_916_H

#include <vector>
#include <string>
#include <unordered_map>
class Solution {
public:
    std::vector<std::string> wordSubsets(std::vector<std::string>& A, std::vector<std::string>& B) {
        std::unordered_map<char,int> UnionB;
        std::vector<std::string> res;
        for (std::string b : B){
            std::unordered_map<char,int> temp;
            for (char c : b){
                if (temp.find(c)!=temp.end()){
                    temp[c]+=1;
                } else{
                    temp.emplace(c,1);
                }
            }
            for(std::unordered_map<char,int>::iterator it=temp.begin();it!=temp.end();++it){
                if (UnionB.find(it->first)!=UnionB.end()){
                    UnionB[it->first]=std::max(temp[it->first],UnionB[it->first]);
                } else{
                    UnionB.emplace(it->first,it->second);
                }
            }
        }
        for (std::string a :A){
            std::unordered_map<char,int> temp;
            bool univer=true;
            for (char c : a){
                if (temp.find(c)!=temp.end()){
                    temp[c]+=1;
                } else{
                    temp.emplace(c,1);
                }
            }
            for(std::unordered_map<char,int>::iterator it=UnionB.begin();it!=UnionB.end();++it){
                if (temp.find(it->first)==temp.end() || temp[it->first]<UnionB[it->first]){
                    univer= false;
                    break;
                }
            }
            if (univer){
                res.push_back(a);
            }
        }
        return res;
    }
};
#endif //CPPVERSION_916_H
