package main

import (
	"fmt"
)

func main() {

	var i int64 = 0
	var vezes int64
	var j1, j2 string

	fmt.Scanln(&vezes)

	for i < vezes {

		fmt.Scanln(&j1)
		fmt.Scanln(&j2)

		if j1 == "ataque" {
			if j2 == "pedra" {
				fmt.Println("Jogador 1 venceu")
			} else if j2 == "papel" {
				fmt.Println("Jogador 1 venceu")
			} else if j2 == "ataque" {
				fmt.Println("Aniquilacao mutua")
			} else {
				continue
			}
		} else if j1 == "pedra" {
			if j2 == "ataque" {
				fmt.Println("Jogador 2 venceu")
			} else if j2 == "papel" {
				fmt.Println("Jogador 1 venceu")
			} else if j2 == "pedra" {
				fmt.Println("Sem ganhador")
			} else {
				continue
			}
		} else if j1 == "papel" {
			if j2 == "ataque" {
				fmt.Println("Jogador 2 venceu")
			} else if j2 == "pedra" {
				fmt.Println("Jogador 2 venceu")
			} else if j2 == "papel" {
				fmt.Println("Ambos venceram")
			} else {
				continue
			}
		} else {
			continue
		}

		i++
	}

}
