package main

import "fmt"

func main() {

	var a []int
	var b []int

	var numero, qtd, i int

	for i = 0; i < 5; i++ {
		fmt.Scanf("%d", &numero)
		a = append(a, numero)
	}

	for i = 0; i < 5; i++ {
		fmt.Scanf("%d", &numero)
		b = append(b, numero)
	}

	for i = 0; i < 5; i++ {
		if a[i] != b[i] {
			qtd++
		}
	}

	if qtd == 5 {
		fmt.Println("Y")
	} else {
		fmt.Println("N")
	}

}
