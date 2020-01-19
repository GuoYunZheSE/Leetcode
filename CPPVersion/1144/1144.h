//
// Created by 郭蕴喆 on 2020/1/19.
//

#ifndef CPPVERSION_1144_H
#define CPPVERSION_1144_H

#include <vector>
#include <string>

class Solution {
public:
    int evenGreaterMoves;
    int oddGreaterMoves;
    Solution(){
        this->evenGreaterMoves=0;
        this->oddGreaterMoves=0;
    }
    void makeEvenGreater(std::vector<int> orign_nums,int index,std::vector<int>* evennums){
        int indexDecrease=0;
        int diff;
        if (index==0){
            diff=orign_nums[0]-orign_nums[1];
            indexDecrease=1;
        } else{
            if (index==orign_nums.size()-1){
                diff=orign_nums[orign_nums.size()-1]-orign_nums[orign_nums.size()-2];
                indexDecrease=orign_nums.size()-2;
            } else{
                if(orign_nums[index]<=orign_nums[index-1]){
                    diff=orign_nums[index]-orign_nums[index-1];
                    this->evenGreaterMoves+=abs(diff)+1;
                    (*evennums)[index-1]=orign_nums[index-1] - abs(diff) - 1;
                }
                if(orign_nums[index]<=orign_nums[index+1]){
                    diff=orign_nums[index]-orign_nums[index+1];
                    this->evenGreaterMoves+=abs(diff)+1;
                    (*evennums)[index+1]=orign_nums[index+1] - abs(diff) - 1;
                }
                diff=1;
            }
        }
        if(diff<=0){
            this->evenGreaterMoves+=abs(diff)+1;
            (*evennums)[indexDecrease] = orign_nums[indexDecrease]-abs(diff)-1;
        }
    }
    void makeOddGreater(std::vector<int> orign_nums,int index,std::vector<int>* oddnums){
        int indexDecrease=0;
        int diff;
        if (index==orign_nums.size()-1){
            diff=orign_nums[orign_nums.size()-1]-orign_nums[orign_nums.size()-2];
            indexDecrease=orign_nums.size()-2;
        } else{
            if(orign_nums[index]<=orign_nums[index-1]){
                diff=orign_nums[index]-orign_nums[index-1];
                this->oddGreaterMoves+=abs(diff)+1;
                (*oddnums)[index-1]=orign_nums[index-1] - abs(diff) - 1;
            }
            if(orign_nums[index]<=orign_nums[index+1]){
                diff=orign_nums[index]-orign_nums[index+1];
                this->oddGreaterMoves+=abs(diff)+1;
                (*oddnums)[index+1]=orign_nums[index+1] - abs(diff) - 1;
            }
            diff=1;
        }
        if(diff<=0){
            this->oddGreaterMoves+=abs(diff)+1;
            (*oddnums)[indexDecrease] = orign_nums[indexDecrease]-abs(diff)-1;
        }
    }

    int movesToMakeZigzag(std::vector<int>& nums) {
        std::vector<int> even_nums=nums;
        std::vector<int> odd_nums=nums;
        int count=0;
        for (std::vector<int>::const_iterator it= nums.begin(); it < nums.end(); ++it) {
            if (count%2==0){
                this->makeEvenGreater(even_nums,count,&even_nums);
            } else{
                this->makeOddGreater(odd_nums,count,&odd_nums);
            }
            count+=1;
        }
        if (this->oddGreaterMoves<this->evenGreaterMoves){
            return this->oddGreaterMoves;
        } else{
            return this->evenGreaterMoves;
        }
    }
};
#endif //CPPVERSION_1144_H
