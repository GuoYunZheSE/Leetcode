//
// Created by 郭蕴喆 on 2020/2/23.
//

#ifndef CPPVERSION_46_H
#define CPPVERSION_46_H

#include <vector>

class Solution {
public:
    void DFS(std::vector<std::vector<int>>& res,const std::vector<int> cur,const std::vector<int>& ans){
        if (cur.empty()){
            res.push_back(ans);
        }
        for (int i = 0; i < cur.size(); ++i) {
            std::vector<int> pre(ans);
            std::vector<int> temp(cur);

            pre.push_back(cur[i]);
            temp.erase(temp.begin()+i);

            this->DFS(res,temp,pre);

        }
    }
    std::vector<std::vector<int>> permute(std::vector<int>& nums) {
        std::vector<std::vector<int>> res;
        std::vector<int> ans;
        this->DFS(res,nums,ans);
        return res;
    }
};
#endif //CPPVERSION_46_H
