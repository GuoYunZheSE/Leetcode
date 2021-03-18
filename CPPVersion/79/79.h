//
// Created by 郭蕴喆 on 2021/3/17.
//

#ifndef CPPVERSION_79_H
#define CPPVERSION_79_H

#endif //CPPVERSION_79_H

#include <vector>
#include <string>
#include <set>
#include <tuple>
#include <unordered_map>

using point = std::tuple<int, int>;

class Solution {
public:
    bool found = false;
    std::set<point> visited = std::set<point>();

    bool contain(int row, int column) {
        auto it = visited.find(point{row, column});
        return !(it == this->visited.end());
    }

    bool preCheck(std::vector<std::vector<char>> &board, const std::string& word){
        std::unordered_map<char,int> bitmap;
        for(auto c : word){
            auto i = bitmap.find(c);
            if (i==bitmap.end()){
                bitmap.emplace(c,1);
            } else{
                i->second+=1;
            }
        }
        for (int row = 0; row < board.size(); ++row) {
            for (int column = 0; column < board[0].size(); ++column) {
                char c = board[row][column];
                auto i = bitmap.find(c);
                if (!(i==bitmap.end())){
                    i->second-=1;
                }
            }
        }
        for(auto & i : bitmap){
            if (i.second>0){
                return false;
            }
        }
        return true;
    }

    void BFS(int row, int column, std::vector<std::vector<char>> &board, std::string word, int index) {
        if (index == word.size()) {
            this->found = true;
            return;
        } else {
            if (!this->found && row < board.size() && column < board[0].size() && word[index] == board[row][column] &&
                !this->contain(row, column)) {
                this->visited.emplace(point{row, column});
                this->BFS(row + 1, column, board, word, index + 1);
                this->BFS(row - 1, column, board, word, index + 1);
                this->BFS(row, column + 1, board, word, index + 1);
                this->BFS(row, column - 1, board, word, index + 1);
                if (!this->found) {
                    this->visited.erase(point{row, column});
                }
            }
        }
    }

    bool exist(std::vector<std::vector<char>> &board, std::string word) {
        if (!preCheck(board,word)){
            return false;
        }
        for (int row = 0; row < board.size(); ++row) {
            for (int column = 0; column < board[0].size(); ++column) {
                this->BFS(row, column, board, word, 0);
                if (this->found) {
                    return true;
                }
            }
        }
        return false;
    }
};