package main

import "fmt"

func main() {

	var x int64
	var i int64 = 0
	var aux int64

	fmt.Scanln(&x)

	for i < 1000 {

		fmt.Printf("N[%d] = %d\n", i, aux)
		aux++

		if x == aux {
			aux = 0
		}

		i++
	}

}
