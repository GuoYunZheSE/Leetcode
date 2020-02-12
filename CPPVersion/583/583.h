//
// Created by 郭蕴喆 on 2020/2/12.
//

#ifndef CPPVERSION_583_H
#define CPPVERSION_583_H

#include <string>
#include <vector>
class Solution {
public:
    int minDistance(std::string word1, std::string word2) {
        std::vector<std::vector<int>> table(word1.size()+1,std::vector<int>(word2.size()+1,0));
        for (int row = 0; row < word1.size(); ++row) {
            for (int column = 0; column < word2.size(); ++column) {
                if (word1[row]==word2[column]){
                    table[row+1][column+1]=table[row][column]+1;
                } else{
                    table[row+1][column+1]=std::max(table[row][column+1],table[row+1][column]);
                }
            }
        }
        return word1.size()+word2.size()-2*table[word1.size()][word2.size()];
    }

};
#endif //CPPVERSION_583_H
