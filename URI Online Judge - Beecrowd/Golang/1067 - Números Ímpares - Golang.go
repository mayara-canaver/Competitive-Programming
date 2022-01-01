package main

import (
	"fmt"
)

func main() {

	var valor int

	fmt.Scanln(&valor)

	for i := 0; i <= valor; i++ {
		if i%2 != 0 {
			fmt.Println(i)
		}
	}

}
