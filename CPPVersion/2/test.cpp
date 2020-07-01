//
// Created by 郭蕴喆 on 2020/7/1.
//

#include "2.h"
#include "gtest/gtest.h"

using namespace std;

//TEST(Longest_Substring_Without_Repeating_Characters,t1){
//    ListNode l2(2,new ListNode(4, new ListNode(3)));
//
//    ListNode l3(5,new ListNode(6,new ListNode(4)));
//
//    Solution s;
//    ListNode* res=s.addTwoNumbers(&l3,&l2);
//    cout<<res->val;
//
//}

TEST(Longest_Substring_Without_Repeating_Characters,t1){
    ListNode l1(5);
    ListNode l2(5);
    Solution s;
    ListNode* res=s.addTwoNumbers(&l1,&l2);
    cout<<res->val;

}
int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}
