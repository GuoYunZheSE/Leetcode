//
// Created by 郭蕴喆 on 2020/1/31.
//

#ifndef CPPVERSION_547_H
#define CPPVERSION_547_H

#include <vector>
#include <set>

class Solution {
public:
    int rows;
    int columns;
    std::set<int> passed;

    void DFS(int r,int c,std::vector<std::vector<int>>& M){
        if (this->passed.find(r)==this->passed.end()){
            this->passed.insert(r);
        }
        if (c<this->columns-1){
            this->DFS(r,c+1,M);
        }
        if (M[r][c]==1){
            if (this->passed.find(c)==this->passed.end()){
                this->DFS(c,0,M);
            }
        }
    }
    int findCircleNum(std::vector<std::vector<int>>& M) {
        this->rows=M.size();
        this->columns=M[0].size();
        int count=0;
        for(int eachRow =0 ; eachRow<M.size();eachRow++){
            if (this->passed.find(eachRow)==this->passed.end()){
                count+=1;
                this->passed.insert(eachRow);
                this->DFS(eachRow,eachRow,M);
            }
        }
        return count;
    }
};
#endif //CPPVERSION_547_H
