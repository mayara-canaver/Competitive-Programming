package main

import "fmt"

func main() {

	var carn, vezes, carneiro int

	fmt.Scanln(&vezes)

	for i := 0; i < vezes; i++ {

		set := make(map[int]bool)
		fmt.Scanln(&carn)

		for j := 0; j < carn; j++ {
			fmt.Scanf("%d", &carneiro)
			set[carneiro] = true
		}
		fmt.Println(len(set))

	}
}
