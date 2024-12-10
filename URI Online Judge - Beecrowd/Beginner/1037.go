package main

import (
	"fmt"
)

func main() {
	var a float64
	fmt.Scanln(&a)

	if 0 <= a && a <= 25 {
		fmt.Println("Intervalo [0,25]")
	} else if 25 < a && a <= 50 {
		fmt.Println("Intervalo (25,50]")
	} else if 50 < a && a <= 75 {
		fmt.Println("Intervalo (50,75]")
	} else if 75 < a && a <= 100 {
		fmt.Println("Intervalo (75,100]")
	} else {
		fmt.Println("Fora de intervalo")
	}

}
