package main

import "fmt"

func main() {

	var i int64 = 0
	var testes, x1, x2 int64

	fmt.Scanln(&testes)

	for i < testes {

		fmt.Scanf("%d %d", &x1, &x2)
		fmt.Printf("%d\n", x1+x2)
		i++
	}

}
