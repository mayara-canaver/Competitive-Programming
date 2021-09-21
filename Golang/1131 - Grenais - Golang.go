package main

import "fmt"

func main() {
	var gol_i, gol_g, total_g, total_i int
	var vezes, qtd_grenal, empate int
	var inter, gremio int

	for {
		fmt.Scanf("%d %d", &gol_i, &gol_g)
		fmt.Scanln(&vezes)

		if gol_i > gol_g {
			inter += 1
		} else if gol_i < gol_g {
			gremio += 1
		} else {
			empate += 1
		}

		fmt.Println("Novo grenal (1-sim 2-nao)")

		qtd_grenal += 1

		if vezes == 2 {
			if inter > gremio {
				total_i += 1
			} else if inter < gremio {
				total_g += 1
			}

			break
		}
	}

	fmt.Printf("%d grenais\n", qtd_grenal)
	fmt.Printf("Inter:%d\n", inter)
	fmt.Printf("Gremio:%d\n", gremio)
	fmt.Printf("Empates:%d\n", empate)

	if total_i > total_g {
		fmt.Println("Inter venceu mais")
	} else if total_i < total_g {
		fmt.Println("Gremio venceu mais")
	} else {
		fmt.Println("Nao houve vencedor")
	}

}
