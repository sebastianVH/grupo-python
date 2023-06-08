# Error: RecursionError: maximum recursion depth exceeded in comparison => es un error que python "ELEVA" par aindicar que hay un bucle infinito

"""
! NameError: intento llamar a una variable que NO EXISTE
! IndexError :el emento al cual se intenta acceder esta fuera de rango
! SyntaxError: hay un error en la sintaxis de lo escrito en el codigo!
! KeyError: intentamos acceder a llave inexistente!
! TypeError: Invalida comparaciones u operaciones entre distintos tipos de dato
! ValueError: estoy intentano utilizar una funcion/metodo sobre un valor el cual es imposible convertir
! ImportError /ModuleNotFound: Estamos intentando importar un modulo inexistente o una funcion inexistente
! ZeroDivisionError: Dividir por 0

"""

# 2/0 => lanza un ZeroDivisionError

lista=["Banana","Manzana"]
#print(lista[6]) => IndexError:el emento al cual se intenta acceder esta fuera del rango de indices

mi_nombre = "Seba"
#print(mi_nombre)

diccionario ={"Nombre":"Seba","Profesion":"Programador"}

#print(diccionario["nombre"]) # KeyError: intentamos acceder a llave inexistente!

#"Hola" + 3 # TypeError => hay un error en el tipo de dato que estamos utilizando

#if "5" < 4: #TypeError => comparacion invalida ENTRE TIPOS DE DATOS
#   print("Si lo eso")

#print(int("Hola")) # ValueError => estoy intentano utilizar una funcion/metodo sobre un valor el cual es imposible convertir

#? TRY - EXCEPT: MANEJO DE EXCEPCIONES:
#Excepcion: es un error elevado por Python para indicarnos algun tipo de problema
#Utilizemos el TRY para evitar que el error aparezca en pantalla:

"""
"try" es una palabra reservada de python que lo que me dice es: "voy a intentar resolver esto"
"except" es una palabra que me dice: Si encuentro tal error al momento de "intentar resolver" , voy a mostrarte un error que me indiques

while True:
    try:
        numero1 = int(input("Ingrese el primer numero: "))
        numero2 = int(input("Ingrese el segundo numero: "))
        resultado = numero1/numero2
        break
    except (ValueError, ZeroDivisionError,NameError) as er :
        print("No pongas letras, o simbolos, soquete!")
        print(er)
        variable = "hola"
        continue
    

print("El resultado es",resultado)
"""
#Clase EXCEPTION

while True:
    try:
        numero1 = input("Ingrese el primer numero: ")
        numero2 = int(input("Ingrese el segundo numero: "))
        if numero1 > numero2:
            print("Es mayor")
        break
    except Exception as error:
        print("Se encontro un error")
        print(error)
        continue

# print("El resultado es",resultado)

"""
HOMEWORK
van a crear variable con los siguientes datos. Cada variable tiene uno de estos datos

var1 = string de mas de un caracter
var2 = string vacio
var3 = Tiene un true
var4 = tiene un False
var5 = tiene un 1 (numerico)
var6 = tiene un 0 (numerico)

*van a comparar los siguientes casos determinando si dan true o false

!para comparar, vamos a crear un if, al cual vamos a poner simplemente la variable.

ej:
if var1:
    print("Es valido")
    
!armar la lista de las que dieron True  y Las que dieron False

*comparar si var2 es igual a var4 y luego var1 igual a var6
*comparar si var1 es igual a var3 y luego si es igual a var6

ej:
if var1 == var2:
    print("Es true")
"""