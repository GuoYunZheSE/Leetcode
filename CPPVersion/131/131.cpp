#include<iostream>

#include<iomanip>

using namespace std;

int main()

{

	double pricep, pricea, numberp, numbera, pay, alreadyget, payp, paya, back;

	cin >> alreadyget >> pricep >> numberp >> pricea >> numbera;

	payp = pricep * numberp;

	paya = pricea * numbera;

	pay = payp + paya;

	back = alreadyget - pay;

	cout << "XXX超市购物小票" << endl;

	cout << "----------------------------------" << endl;

	cout << "物品名称" << " " << "单价" << " " << "数量" << " " << "金额" << endl;

	cout << "花生" << "     " << fixed << setprecision(2) << pricep << " " << numberp << " " << payp << endl;

	cout << "苹果" << "     " << fixed << setprecision(2) << pricea << " " << numbera << " " << paya << endl;

	cout << " ----------------------------------" << endl;

	cout << "已收： ￥" << fixed << setprecision(2) << alreadyget << "元" << endl;

	cout << "实收： ￥" << fixed << setprecision(2) << pay << "元" << endl;

	cout << "找零： ￥" << fixed << setprecision(2) << back << "元" << endl;

	return 0;

}

