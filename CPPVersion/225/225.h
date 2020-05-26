//
// Created by 郭蕴喆 on 2020/5/24.
//

#ifndef CPPVERSION_225_H
#define CPPVERSION_225_H

#endif //CPPVERSION_225_H

#include <queue>

class MyStack {
public:
    std::queue<int> stack;
    /** Initialize your data structure here. */
    MyStack() {
    }

    /** Push element x onto stack. */
    void push(int x) {
        this->stack.push(x);
    }

    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int ans=this->stack.back();
        std::queue<int> temp;
        if(this->stack.empty()){
            return -1
        }
        for (int i = 0; i < this->stack.size()-1; ++i) {
            int front=this->stack.front();
            this->stack.pop();
            temp.push(front);
        }
        this->stack=temp;
        return ans;
    }

    /** Get the top element. */
    int top() {
        return this->stack.back();
    }

    /** Returns whether the stack is empty. */
    bool empty() {
        return this->stack.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */