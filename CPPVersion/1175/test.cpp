//
// Created by 郭蕴喆 on 2020/1/21.
//

#include "1175.h"
#include <gtest/gtest.h>
using namespace std;

TEST(PA,t1){
    Solution sol;
    int res=sol.numPrimeArrangements(5);
    EXPECT_EQ(12,res);
}
TEST(PA,t2){
    Solution sol;
    int res=sol.numPrimeArrangements(6);
    EXPECT_EQ(36,res);
}
TEST(PA,t3){
    Solution sol;
    int res=sol.numPrimeArrangements(4);
    EXPECT_EQ(4,res);
}
TEST(PA,t4){
    Solution sol;
    int res=sol.numPrimeArrangements(100);
    EXPECT_EQ(682289015,res);
}
int main(int argc, char ** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}