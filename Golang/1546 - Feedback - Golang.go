package main

import "fmt"

func main() {

	var vezes, dias, feedback int

	fmt.Scanln(&dias)

	for i := 0; i < dias; i++ {

		fmt.Scanln(&vezes)

		for j := 0; j < vezes; j++ {

			fmt.Scanln(&feedback)

			if feedback == 1 {
				fmt.Println("Rolien")
			} else if feedback == 2 {
				fmt.Println("Naej")
			} else if feedback == 3 {
				fmt.Println("Elehcim")
			} else {
				fmt.Println("Odranoel")
			}

		}

	}

}
