package main

import "fmt"

func main() {

	var n, m int
	var jogos, qtd, total int

	fmt.Scanf("%d %d", &n, &m)

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			fmt.Scanf("%d", &jogos)

			if jogos > 0 {
				qtd++
			}
		}
		if qtd == m {
			total++
		}

		qtd = 0

	}

	fmt.Println(total)

}
