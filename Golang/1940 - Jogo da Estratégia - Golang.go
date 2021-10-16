package main

import "fmt"

var m map[int]int

func main() {
	m = make(map[int]int)
	var jog, r, ponto, aux, jogador int

	fmt.Scanf("%d %d", &jog, &r)

	for j := 0; j < r; j++ {

		for i := 0; i < jog; i++ {
			fmt.Scanf("%d", &ponto)
			m[i] += ponto
		}
	}

	aux = -1

	for i := (jog - 1); i >= 0; i-- {
		if m[i] > aux {
			aux = m[i]
			jogador = i
		}
	}

	fmt.Println(jogador + 1)

}
