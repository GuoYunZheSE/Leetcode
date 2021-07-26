// 学号201936501443   姓名：陶行健   班级：数学4班

#include <iostream>
#include<cmath>
using namespace std;


double function(double x)  //定义函数f（x）
{
    return (1 + 2 * x * x + 3 * x * x * x);
}



double integralValue(double a, double b,int N)  //求定积分
{
    double dx = (b - a) / N;
    double sum = 0;
    for (int n = 0; n <= N; n++)
    {
        sum += dx * ((function(a + n * dx)) + function(a + (n + 1) * dx)) / 2;
    }
    return sum;
}

int main()
{
    double a, b;
    int N;
    cout << "请输入积分上限：";
    cin >> b;
    cout << "请输入积分下限：";
    cin >> a;
    cout << "请输入积分区间数：";
    cin >> N;
    cout << "积分结果等于：" << integralValue(a, b, N);
    return 0;
}