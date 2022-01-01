package main

import "fmt"

func main() {
	var raio float64
	var area float64
	pi := 3.14159
	fmt.Scanf("%f", &raio)
	area = pi * raio * raio
	fmt.Printf("A=%.4f\n", area)

}
