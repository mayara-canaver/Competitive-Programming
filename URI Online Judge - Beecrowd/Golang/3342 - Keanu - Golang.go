package main

import "fmt"

func main() {

	var numero int

	fmt.Scanf("%d", &numero)

  numero = (numero * numero)

  if (numero % 2 == 0){
    fmt.Printf("%d casas brancas e %d casas pretas\n", numero / 2, numero / 2)
  }else{
    fmt.Printf("%d casas brancas e %d casas pretas\n", (numero / 2) + 1, numero / 2)
  }
  
}
