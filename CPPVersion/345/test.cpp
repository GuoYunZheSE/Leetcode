//
// Created by 郭蕴喆 on 2019/12/18.
//

#include "345.h"
#include <gtest/gtest.h>

TEST(RVos,t1){
    Solution s;
    EXPECT_EQ("holle",s.reverseVowels("hello"));
}

int main(int argc, char ** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}