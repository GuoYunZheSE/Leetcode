//
// Created by 郭蕴喆 on 2020/2/27.
//

#include <gtest/gtest.h>
#include "916.h"

using namespace std;

TEST(wordSubsets,t1){
    Solution s;
    vector<string> A({"amazon","apple","facebook","google","leetcode"});
    vector<string> B({"e","o"});
    vector<string> res({"facebook","google","leetcode"});
    EXPECT_EQ(res,s.wordSubsets(A,B));
}
TEST(wordSubsets,t2){
    Solution s;
    vector<string> A({"amazon","apple","facebook","google","leetcode"});
    vector<string> B({"l","e"});
    vector<string> res({"apple","google","leetcode"});
    EXPECT_EQ(res,s.wordSubsets(A,B));
}
TEST(wordSubsets,t3){
    Solution s;
    vector<string> A({"amazon","apple","facebook","google","leetcode"});
    vector<string> B({"lo","eo"});
    vector<string> res({"google","leetcode"});
    EXPECT_EQ(res,s.wordSubsets(A,B));
}
TEST(wordSubsets,t4){
    Solution s;
    vector<string> A({"amazon","apple","facebook","google","leetcode"});
    vector<string> B({"e","oo"});
    vector<string> res({"facebook","google"});
    EXPECT_EQ(res,s.wordSubsets(A,B));
}
TEST(wordSubsets,t5){
    Solution s;
    vector<string> A({"amazon","apple","facebook","google","leetcode"});
    vector<string> B({"ec","oc","ceo"});
    vector<string> res({"facebook","leetcode"});
    EXPECT_EQ(res,s.wordSubsets(A,B));
}
int main(int argc, char ** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}