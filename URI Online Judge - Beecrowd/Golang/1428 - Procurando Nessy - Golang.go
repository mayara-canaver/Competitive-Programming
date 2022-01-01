package main

import "fmt"

func main() {

	var n, m, vezes int

	fmt.Scanln(&vezes)

	for i := 0; i < vezes; i++ {

		fmt.Scanf("%d %d", &n, &m)

		fmt.Println((n / 3) * (m / 3))

	}

}
