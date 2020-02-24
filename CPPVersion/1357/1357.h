//
// Created by 郭蕴喆 on 2020/2/24.
//

#ifndef CPPVERSION_1357_H
#define CPPVERSION_1357_H

#include <vector>
#include <unordered_map>

class Cashier {
public:
    int n;
    int discount;
    int sum=0;
    std::unordered_map<int,int> list;
    Cashier(int n, int discount, std::vector<int>& products, std::vector<int>& prices) {
        this->n=n;
        this->discount=discount;
        for(int i=0;i<prices.size();++i){
            this->list.insert({products[i],prices[i]});
        }
    }

    double getBill(std::vector<int> product, std::vector<int> amount) {
        this->sum+=1;
        double bill=0.0;
        for (int i = 0; i < product.size(); ++i) {
            bill+=amount[i]*this->list[product[i]];
        }
        if (this->sum==this->n){
            this->sum=0;
            bill-=((this->discount*bill)/100);
        }
        return bill;
    }
};

#endif //CPPVERSION_1357_H
