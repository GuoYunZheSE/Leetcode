//
// Created by 郭蕴喆 on 2019/11/27.
//

#include "731.h"
#include <gtest/gtest.h>


TEST(MyCalendarTwo,t1){
    MyCalendarTwo s;
    EXPECT_TRUE(s.book(10,20));
    EXPECT_TRUE(s.book(20,30));
    EXPECT_TRUE(s.book(10,15));
    EXPECT_FALSE(s.book(11,12));
}
int main(int argc, char ** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}