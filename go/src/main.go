package main

import (
	"fmt"
	"strconv"
)

//Variables globales
var (
	nombre        string = "Julio"
	apellido      string = "Preciado"
	edad          int    = 22
	mesNacimiento int    = 4
)

func main() {
	// Variables en GOALNGS
	var i int
	i = 1
	var j float32 = 2
	k := 13.54

	//Imprimir variable y su tipo de dato
	fmt.Println("\n-----------------------")
	fmt.Printf("%v, %T", i, i)
	fmt.Printf("%v, %T", j, j)
	fmt.Printf("%v, %T", k, k)

	//Imprimir variables globales
	fmt.Println("\n-----------------------")
	fmt.Println(nombre)

	//Castear variables
	fmt.Println("\n-----------------------")
	var l int
	l = int(k)
	fmt.Printf("%v, %T", l, l)

	//Castear entero a string
	//Cuando casteas un entero a un string el número casteado regresa el unicode
	//Example:
	fmt.Println("\n-----------------------")
	var arroba int = 64
	var ascii string
	ascii = string(arroba)
	fmt.Println(ascii)

	//Para pasar un entero a un string sin aparezca el ascii
	fmt.Println("\n-----------------------")
	var texto string
	texto = strconv.Itoa(arroba)
	fmt.Println(texto)

	//Variables primitivas
	fmt.Println("\n-----------------------")
	var n bool = true //false
	fmt.Println(n)
	ternario := 1 == 2
	fmt.Println(ternario)

	//Operaciones Básicas
	fmt.Println("\n-----------------------")
	a := 10 // 1010
	b := 3  // 0011
	c := 8  // 2^3
	fmt.Println(a + b)
	fmt.Println(a - b)
	fmt.Println(a * b)
	fmt.Println(a / b)
	fmt.Println(a % b)

	//Operaciones propias de GO
	fmt.Println("\n-----------------------")
	fmt.Println(a & b)  // 0010
	fmt.Println(a | b)  // 1011
	fmt.Println(a ^ b)  // 1001
	fmt.Println(a &^ b) // 0100
	fmt.Println(c >> 3) // 2^3 * 2^3 = 2^6
	fmt.Println(c << 3) // 2^3 / 2^3 = 2^0

	//

}
