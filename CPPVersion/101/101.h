//
// Created by 郭蕴喆 on 2021/3/30.
//

#ifndef CPPVERSION_101_H
#define CPPVERSION_101_H

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
    bool valid = true;
    void compare(TreeNode* left, TreeNode* right){
        if (!this->valid){
            return;
        }
        if (left== nullptr && right== nullptr){
            return;
        }
        if (left== nullptr || right== nullptr){
            this->valid= false;
            return;
        }
        this->valid=(left->val==right->val);
        this->compare(left->left,right->right);
        this->compare(left->right,right->left);
   }
    bool isSymmetric(TreeNode* root) {
        this->compare(root->left,root->right);
        return this->valid;
    }
};
#endif //CPPVERSION_101_H
