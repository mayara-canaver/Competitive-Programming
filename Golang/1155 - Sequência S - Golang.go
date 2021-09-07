package main

import "fmt"

func main() {

	var total, i float64

	for i = 1; i <= 100; i++ {

		total += (1 / i)

	}

	fmt.Printf("%.2f\n", total)

}
