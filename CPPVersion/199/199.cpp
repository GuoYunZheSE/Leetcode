//
// Created by 郭蕴喆 on 2019/11/20.
//

#include "199.h"
#include <iostream>

vector<int> Solution::rightSideView(TreeNode *root) {
    if (root == NULL){
        vector<int> temp;
        return temp;
    }

    this->updateDic(root->val,0);
    int currentDepth=0;
    this->iterTree(root,currentDepth);
    int Depth=0;
    vector<int> ans;

    for (unordered_map<int,vector<int>>::const_iterator it=this->res.begin();it!=this->res.end();it++){
        if(it->first>=Depth){
            Depth=it->first;
        }
    }
    for(int i=0;i<=Depth;i++){
        ans.push_back(this->res[i].back());
    }
    return ans;
}

void Solution::updateDic(int A, int Length) {
    unordered_map<int,vector<int>>::const_iterator got=this->res.find(Length);
    if(got==this->res.end()){
        vector<int> temp(1,A);
        this->res.insert({Length,temp});
    } else{
        vector<int> temp=got->second;
        temp.push_back(A);
        this->res.erase(Length);
        this->res.insert({Length,temp});
    }
}

void Solution::iterTree(TreeNode *node, int currentDepth) {
    if(node->left != NULL){
        this->iterTree(node->left,currentDepth+1);
    }
    this->updateDic(node->val,currentDepth);
    if(node->right!=NULL){
        this->iterTree(node->right,currentDepth+1);
    }
}

void Solution::test(TreeNode *node) {
   vector<int> temp=this->rightSideView(node);
    for (vector<int>::const_iterator it=temp.begin();it!=temp.end();it++){
        cout<<' '<<*it;
    }
}

