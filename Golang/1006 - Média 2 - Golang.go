package main

import "fmt"

func main() {
	var a float64
	var b float64
	var c float64
	var media float64
	fmt.Scanln(&a)
	fmt.Scanln(&b)
	fmt.Scanln(&c)
	media = (a*2 + b*3 + c*5) / 10
	fmt.Printf("MEDIA = %.1f\n", media)

}
