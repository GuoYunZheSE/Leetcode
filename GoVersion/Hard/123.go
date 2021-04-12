package main

func max(a int, b int)  int{
	if (a>=b){
		return a
	}
	return b
}

func min(a int, b int)  int{
	if (a>=b){
		return b
	}
	return a
}

func maxProfit(prices []int) int {
	first_buy:=10000000
	first_sell:=-1000000
	second_buy:=-1000000
	second_sell:=-10000000

	for i:=0;i<len(prices);i+=1{
		first_buy=min(first_buy,prices[i])
		first_sell=max(first_sell,prices[i]-first_buy)
		second_buy=max(second_buy,first_sell-prices[i])
		second_sell=max(second_sell,prices[i]+second_buy)
	}
	return second_sell
}