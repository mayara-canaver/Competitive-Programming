package main

import "fmt"

func main() {

	var numero, i int

	for i = 1; i <= 4; i++ {
		fmt.Scanf("%d", &numero)
		if numero == 1 {
			fmt.Println(i)
		}
	}

}
