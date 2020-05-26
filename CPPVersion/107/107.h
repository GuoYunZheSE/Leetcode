//
// Created by 郭蕴喆 on 2020/5/26.
//

#ifndef CPPVERSION_107_H
#define CPPVERSION_107_H

#endif //CPPVERSION_107_H

#include <vector>
#include <unordered_map>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    std::unordered_map<int,std::vector<int>> dict;
    int maxDepth=0;
    void DFS(TreeNode* cur,int depth){
        std::unordered_map<int,std::vector<int>>::const_iterator got = dict.find (depth);
        this->maxDepth=std::max(this->maxDepth,depth);
        if (got!=dict.end()){
            dict[depth].push_back(cur->val);
        } else{
            dict.emplace(depth,std::vector<int>({cur->val}));
        }
        if (cur->left){
            this->DFS(cur->left,depth+1);
        }
        if (cur->right){
            this->DFS(cur->right,depth+1);
        }

    }
    std::vector<std::vector<int>> levelOrderBottom(TreeNode* root) {
        std::vector<std::vector<int>> ans;
        if (!root){
            return ans;
        }
        this->DFS(root,0);
        for (int i = this->maxDepth; i > -1; --i) {
            ans.push_back(this->dict[i]);
        }
        return ans;
    }
};