//
// Created by 郭蕴喆 on 2020/1/29.
//

#ifndef CPPVERSION_542_H
#define CPPVERSION_542_H

#include <vector>
class Solution {
public:
    int rows;
    int columns;
    std::vector<std::vector<int>> matrix;
    int BFS(int r, int c){
        int hip=1;
        while (true){
            for (int rowChange = -hip; rowChange <hip+1 ; ++rowChange) {
                if((r+rowChange)>=0 && (r+rowChange)<this->rows){
                    if((c+abs(hip-abs(rowChange)))<this->columns){
                        if(this->matrix[r+rowChange][c+abs(hip-abs(rowChange))]==0){
                            return hip;
                        }
                    }
                    if((c-abs(hip-abs(rowChange)))>=0){
                        if(this->matrix[r+rowChange][c-abs(hip-abs(rowChange))]==0){
                            return hip;
                        }
                    }
                }
            }
            hip+=1;
        }
    }
    std::vector<std::vector<int>> updateMatrix(std::vector<std::vector<int>>& matrix1) {
        this->rows=matrix1.size();
        this->columns=matrix1[0].size();
        this->matrix=matrix1;
        std::vector<std::vector<int>> res=matrix1;
        for(int eachRow=0;eachRow<this->rows;eachRow++){
            for(int eachColumn=0;eachColumn<this->columns;eachColumn++){
                if(this->matrix[eachRow][eachColumn]!=0){
                    res[eachRow][eachColumn]=this->BFS(eachRow,eachColumn);
                }
            }
        }
        return res;
    }
};
#endif //CPPVERSION_542_H
