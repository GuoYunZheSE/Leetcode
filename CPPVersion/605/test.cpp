//
// Created by 郭蕴喆 on 2020/2/4.
//

#include <gtest/gtest.h>
#include "605.h"

using namespace std;

TEST(CPF,t1){
    vector<int> num({1,0,0,0,1});
    Solution s;
    EXPECT_TRUE(s.canPlaceFlowers(num,1));
}
TEST(CPF,t2){
    vector<int> num({1,0,0,0,1});
    Solution s;
    EXPECT_FALSE(s.canPlaceFlowers(num,2));
}

int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}