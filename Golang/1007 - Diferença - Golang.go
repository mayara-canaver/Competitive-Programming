package main

import "fmt"

func main() {
	var a int
	var b int
	var c int
	var d int
	var media int
	fmt.Scanln(&a)
	fmt.Scanln(&b)
	fmt.Scanln(&c)
	fmt.Scanln(&d)
	media = (a*b - c*d)
	fmt.Printf("DIFERENCA = %d\n", media)

}
