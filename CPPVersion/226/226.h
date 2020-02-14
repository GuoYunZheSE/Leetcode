//
// Created by 郭蕴喆 on 2020/2/14.
//

#ifndef CPPVERSION_226_H
#define CPPVERSION_226_H

#include <opencl-c.h>

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    void preorder(TreeNode* root){
        TreeNode* temp=root->left;
        root->left=root->right;
        root->right=temp;
        if (root->left){
            this->preorder(root->left);
        }
        if (root->right){
            this->preorder(root->right);
        }
    }
    TreeNode* invertTree(TreeNode* root) {
        if (root==nullptr){
            return root;
        }
        this->preorder(root);
        return root;
    }
};
#endif //CPPVERSION_226_H
