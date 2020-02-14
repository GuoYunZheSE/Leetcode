//
// Created by 郭蕴喆 on 2020/2/14.
//

#ifndef CPPVERSION_206_H
#define CPPVERSION_206_H

struct ListNode {
         int val;
         ListNode *next;
         ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head== nullptr){
            return head;
        }
        ListNode* pre= nullptr;
        while (head->next!= nullptr){
            ListNode* rest=head->next;
            head->next=pre;
            pre=head;
            head=rest;
        }
        head->next=pre;
        return head;
    }
};
#endif //CPPVERSION_206_H
