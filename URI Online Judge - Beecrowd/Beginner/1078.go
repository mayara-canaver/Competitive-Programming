package main

import (
	"fmt"
)

func main() {

	var vezes int64
	var i int64

	fmt.Scanln(&vezes)

	for i = 1; i <= 10; i++ {

		fmt.Printf("%d x %d = %d\n", i, vezes, i*vezes)

	}
}
