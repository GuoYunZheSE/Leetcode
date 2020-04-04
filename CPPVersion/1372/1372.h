//
// Created by 郭蕴喆 on 2020/3/19.
//

#ifndef CPPVERSION_1372_H
#define CPPVERSION_1372_H
#include <algorithm>
#endif //CPPVERSION_1372_H

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 };

class Solution {
public:
    int depth=0;
    void DFS(TreeNode* root, bool last_is_left, int depth){
        this->depth=std::max(depth,this->depth);
        if(root== nullptr){
            return;
        } else{
            if (last_is_left){
                this->DFS(root->left, true,0);
                this->DFS(root->right, false,depth+1);
            } else{
                this->DFS(root->right, false,0);
                this->DFS(root->left, true,depth+1);
            }
        }
    }
    int longestZigZag(TreeNode* root) {
        this->DFS(root->left, true,0);
        this->DFS(root->right, false,0);
        return this->depth;
    }
};