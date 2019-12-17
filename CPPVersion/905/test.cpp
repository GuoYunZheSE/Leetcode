//
// Created by 郭蕴喆 on 2019/12/13.
//

#include <gtest/gtest.h>
#include "905.h"

TEST(SABP,t1){
    Solution s;
    int myints[]={3,1,2,4};
    std::vector<int> v (myints,myints + sizeof(myints) / sizeof(int) );
    s.sortArrayByParity(v);
}
int main(int argc, char ** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}