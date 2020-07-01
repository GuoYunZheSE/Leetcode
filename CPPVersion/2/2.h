//
// Created by 郭蕴喆 on 2020/7/1.
//

#ifndef CPPVERSION_2_H
#define CPPVERSION_2_H

#include <vector>
struct ListNode {
 int val;
 ListNode *next;
 ListNode() : val(0), next(nullptr) {}
 ListNode(int x) : val(x), next(nullptr) {}
 ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carried=0;
        std::vector<int> res({0});
        while(l1 || l2){
            if (l1!= nullptr){
                res[res.size()-1]+=l1->val;
                l1=l1->next;
            }
            if (l2!= nullptr){
                res[res.size()-1]+=l2->val;
                l2=l2->next;
            }
            res[res.size()-1]+=carried;
            carried=0;
            if ( res[res.size()-1]>=10){
                res[res.size()-1]-=10;
                carried+=1;
            }
            if (l1||l2){
                res.push_back(0);
            } else{
                if (carried!=0){
                    res.push_back(1);
                    break;
                }
            }
        }
        ListNode* lres=new ListNode(res[0]);
        ListNode* head=lres;
        for (int i = 1; i < res.size(); ++i) {
            lres->next=new ListNode(res[i]);
            lres=lres->next;
        }
        return head;
    }
};
#endif //CPPVERSION_2_H
