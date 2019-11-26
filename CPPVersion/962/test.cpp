//
// Created by 郭蕴喆 on 2019/11/23.
//

#include <gtest/gtest.h>
#include "962.h"

TEST(maxWidthRamp,t1){
    Solution s;
    int temp[]={1,0};
    vector<int> A(temp,temp+ sizeof(temp)/ sizeof(int));
    EXPECT_EQ(0,s.maxWidthRamp(A));
}

TEST(maxWidthRamp,t2){
    Solution s;
    int temp[]={6,0,8,2,1,5};
    vector<int> A(temp,temp+ sizeof(temp)/ sizeof(int));
    EXPECT_EQ(4,s.maxWidthRamp(A));
}


//int main(int argc, char ** argv) {
//    testing::InitGoogleTest(&argc, argv);
//    return RUN_ALL_TESTS();  // 执行所有的 test case
//}