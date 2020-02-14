//
// Created by 郭蕴喆 on 2020/2/14.
//

#ifndef CPPVERSION_92_H
#define CPPVERSION_92_H

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if (head== nullptr or m==n){
            return head;
        }
        ListNode* pre= nullptr;
        ListNode* reverse= head;
        if (m!=1){
            pre=head;
            for (int i = 1; i < m-1; ++i) {
                pre=pre->next;
            }
            reverse=pre->next;
        }

        ListNode* rest= reverse;
        for (int j=0;j<n-m+1;j++){
            rest=rest->next;
        }
        int length=0;
        while (length<n-m+1){
            length+=1;
            ListNode* temp=reverse->next;
            reverse->next=rest;
            rest=reverse;
            reverse=temp;
        }
        if (pre== nullptr){
            return rest;
        } else{
            pre->next=rest;
            return head;
        }
    }
};
#endif //CPPVERSION_92_H
