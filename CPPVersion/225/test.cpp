//
// Created by 郭蕴喆 on 2020/5/25.
//

#include "225.h"
#include "gtest/gtest.h"

using namespace std;

TEST(MyStack,t1){
    MyStack s;
    s.push(1);
    s.push(2);
    s.push(3);
    s.pop();
    s.pop();
    s.pop();
    s.empty();
}

int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}
