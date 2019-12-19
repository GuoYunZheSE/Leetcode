//
// Created by 郭蕴喆 on 2019/12/19.
//

#ifndef CPPVERSION_1110_H
#define CPPVERSION_1110_H

#endif //CPPVERSION_1110_H

#include <vector>
#include <unordered_set>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    std::unordered_set<int> to_delete_set;
    std::vector<TreeNode*> roots;
    std::vector<TreeNode*> find_roots(TreeNode* root, std::vector<TreeNode*>& temp){
        if(this->to_delete_set.find(root->val)!=this->to_delete_set.end()){
            if(root->left!=NULL){
                this->find_roots(root->left,temp);
            }
            if(root->right!=NULL){
                this->find_roots(root->right,temp);
            }
        } else{
            temp.push_back(root);
        }
        return temp;
    }
    void DFS(TreeNode* root){
        if(root->left!=NULL){
            if(this->to_delete_set.find(root->left->val)==this->to_delete_set.end()){
                this->DFS(root->left);
            } else{
                if(root->left->left != NULL){
                    std::vector<TreeNode*> Temp;
                    this->find_roots(root->left->left,Temp);
                    this->roots.insert(this->roots.end(),Temp.begin(),Temp.end());
                }
                if (root->left->right !=NULL){
                    std::vector<TreeNode*> Temp;
                    this->find_roots(root->left->right,Temp);
                    this->roots.insert(this->roots.end(),Temp.begin(),Temp.end());
                }
                root->left=NULL;
            }
        }
        if(root->right!=NULL){
            if(this->to_delete_set.find(root->right->val)==this->to_delete_set.end()){
                this->DFS(root->right);
            } else{
                if(root->right->left!=NULL){
                    std::vector<TreeNode*> Temp;
                    this->find_roots(root->right->left,Temp);
                    this->roots.insert(this->roots.end(),Temp.begin(),Temp.end());
                }
                if (root->right->right!=NULL){
                    std::vector<TreeNode*> Temp;
                    this->find_roots(root->right->right,Temp);
                    this->roots.insert(this->roots.end(),Temp.begin(),Temp.end());
                }
                root->right=NULL;
            }
        }
    }
    std::vector<TreeNode*> delNodes(TreeNode* root, std::vector<int>& to_delete) {
        for (int i = 0; i < to_delete.size(); ++i) {
            this->to_delete_set.insert(this->to_delete_set.end(),to_delete[i]);
        }
        std::vector<TreeNode*> Temp;
        this->find_roots(root,Temp);
        this->roots.insert(this->roots.end(),Temp.begin(),Temp.end());
        for(std::vector<TreeNode*>::iterator it =this->roots.begin();it!=this->roots.end();it++){
            this->DFS(*it);
        }
        return this->roots;
    }
};