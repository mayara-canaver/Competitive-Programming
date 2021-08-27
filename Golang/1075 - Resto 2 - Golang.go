package main

import (
	"fmt"
)

func main() {

	var vezes int64
	var i int64

	fmt.Scanln(&vezes)

	for i = 1; i <= 10000; i++ {

		if i%vezes == 2 {

			fmt.Println(i)

		}

	}

}
