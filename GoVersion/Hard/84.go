package main

import (
	"fmt"
	"math"
)

func largestRectangleArea(heights []int) int {
	var stack [] int
	stack=append(stack, 0)
	heights=append(heights,0)
	res:=0

	for i:=0;i<len(heights);i+=1{
		if len(stack)>1{
			j:=stack[len(stack)-1]
			for j>=0 && heights[i]<heights[j]{
				height:=heights[j]
				stack=stack[:len(stack)-1]
				width:=i-stack[len(stack)-1]-1
				res= int(math.Max(float64(res), float64(height*width)))
				fmt.Println(height,width,res)
				j=stack[len(stack)-1]
			}
		}
		stack=append(stack,i)
	}
	return res
}


