package main

import "fmt"

func main() {

	var x int64
	var i int64 = 0

	fmt.Scanln(&x)

	for i < 10 {
		fmt.Printf("N[%d] = %d\n", i, x)
		x *= 2
		i++
	}

}
