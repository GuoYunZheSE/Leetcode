package main

import (
	"fmt"
	"strconv"
)

func numDecodings(s string) int {
	res:=make([]int, len(s)+1, len(s)+1)
	for i:=0;i< len(res);i+=1{
		res[i]=0
	}
	res[0]=1
	res[1]=1
	if s[0:1]=="0"{
		res[1]=0
		return 0
	}
	for j:=2;j<len(s)+1;j+=1{
		single,_:=strconv.Atoi(s[j-1:j])
		if 0<single && single<=9{
			res[j]+=res[j-1]
		}
		double,_:=strconv.Atoi(s[j-2:j])
		if 10<=double && double<=26{
			res[j]+=res[j-2]
		}
	}
	return res[len(res)-1]
}





func main()  {
	fmt.Println(numDecodings("0"))
}