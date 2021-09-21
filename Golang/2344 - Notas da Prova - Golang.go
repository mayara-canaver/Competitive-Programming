package main

import "fmt"

func main() {

	nota := 0

	fmt.Scanln(&nota)

	if nota == 0 {
		fmt.Println("E")
	} else if nota > 0 && nota <= 35 {
		fmt.Println("D")

	} else if nota > 35 && nota <= 60 {
		fmt.Println("C")

	} else if nota > 60 && nota <= 85 {
		fmt.Println("B")

	} else {
		fmt.Println("A")

	}

}
