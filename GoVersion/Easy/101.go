package main

import (
	"fmt"
)

var ch = make(chan int)

func print5(i int) {
	<-ch
	fmt.Println(i)
}

func main() {
	fmt.Println("Start print 75")

	for i := 1; i <= 75; i ++ {
		go print5(i)
		ch <- 1
	}

	fmt.Println("End print 75")
}