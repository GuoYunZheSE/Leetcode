//
// Created by 郭蕴喆 on 2020/2/14.
//

#ifndef CPPVERSION_141_H
#define CPPVERSION_141_H
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head== nullptr){
            return false;
        }
        ListNode* OneStep=head;
        ListNode* TwoStep=head;
        while (TwoStep->next != nullptr && TwoStep->next->next!= nullptr){
            OneStep=OneStep->next;
            TwoStep=TwoStep->next->next;
            if (OneStep==TwoStep){
                return true;
            }

        }
        return false;
    }
};
#endif //CPPVERSION_141_H
