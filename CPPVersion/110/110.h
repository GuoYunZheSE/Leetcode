//
// Created by 郭蕴喆 on 2021/3/30.
//

#ifndef CPPVERSION_110_H
#define CPPVERSION_110_H

#include <cstdlib>
#include <algorithm>

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
    int DFS(TreeNode* root){
        if (root== nullptr){
            return 0;
        } else{
            int leftheight=DFS(root->left);
            int rightheight=DFS(root->right);
            if (leftheight==-1 || rightheight==-1){
                return -1;
            }
            if (abs(leftheight-rightheight)>1){
                return -1;
            }
            return std::max(leftheight,rightheight)+1;
        }
    }
    bool isBalanced(TreeNode* root) {
        if (root== nullptr){
            return true;
        }
        int res=this->DFS(root);
        return res!=-1;
    }
};
#endif //CPPVERSION_110_H
