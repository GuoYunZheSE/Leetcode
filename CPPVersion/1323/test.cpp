//
// Created by 郭蕴喆 on 2020/1/23.
//

#include "1323.h"
#include "gtest/gtest.h"

TEST(M69N,t1){
    Solution s;
    EXPECT_EQ(9969,s.maximum69Number(9669));
}
TEST(M69N,t2){
    Solution s;
    EXPECT_EQ(9999,s.maximum69Number(9999));
}
TEST(M69N,t3){
    Solution s;
    EXPECT_EQ(9999,s.maximum69Number(9996));
}
int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}