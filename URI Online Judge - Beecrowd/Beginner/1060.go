package main

import (
	"fmt"
)

func main() {
	var valor float64
	var contador int64

	for i := 1; i <= 6; i++ {

		fmt.Scanln(&valor)
		if valor > 0 {
			contador++
		}

	}

	fmt.Printf("%d valores positivos\n", contador)

}
