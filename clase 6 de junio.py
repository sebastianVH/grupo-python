#RECURSIVIDAD: Una funcion recursiva es una funcion la cual se llama asi misma

#crear una funcion que simule la multiplicacion: ej: si pongo en mi funcion 5 y 8, me devuelve 40

#! en una recursividad SIEMPRE EXISTE UN CASO DE CORTE
#? EN EL RETURN SE INVOCA/LLAMA A SI MISMA

"""
* 5 x 8 => 5+5+5+5+5+5+5+5
* 6 x 3 => 6+6+6
* 7 x 4 => 7+7+7+7
"""

def multiplicar(base,multiplicador):
    if multiplicador > 1:
        return base + multiplicar(base,multiplicador-1)
    return base

#  multiplicar(3,5) => 3 + multiplicar(3,4) => 
#  3 + ( 3 + multiplicar(3,3)) 
#  3 + ( 3 + ( 3 + multiplicar(3,2)))
#  3 + ( 3 + ( 3 + 3 + multiplicar(3,1)))
#  3 + ( 3 + ( 3 + 3 + (3)))

#!print(multiplicar(7,7))

#?----- FACTORIAL ----------#
#es una multiplicacion sucesiva descendiente hasta 1 de un numero

#factorial = !5 => 5x4x3x2x1 => 120
#factorial = !7 => 7x6x5x4x3x2x1 => 5040
#factorial = !4 => 4x3x2x1 => 24

def factorial(numero):
    if numero > 1:
        return numero * factorial(numero-1)
    return 1

# operador ternario: return 1 if numero <=1 else numero * factorial(numero-1)

#print(factorial(9))

#factorial(5) => 5 * factorial(4)
#factorial(4) => 4 * factorial(3)
#factorial(3) => 3 * factorial(2)
#factorial(2) => 2 * 1
#factorial(1) => 1

#? sacar una potencia:
#una potencia es un numero multiplicado por si mismo una determinada cant de veces
""" 
ej 3**4 => 3x3x3x3 
5**3 => 5x5x5
"""

# def potencia(base,exponente):
#     if exponente > 1:
#         return base * potencia(base,exponente-1)
#     return base
    
def potencia(base,exponente):
    if exponente < 0:
        return("No ingrese numeros negativos")
    if exponente == 0: 
        return 1
    if exponente == 1:
        return base
    return base * potencia(base,exponente-1)
    
"""
def multiplicar(base,multiplicador):
    if multiplicador > 1:
        return base + multiplicar(base,multiplicador-1)
    return base
"""
print(potencia(3,8))

#TODO: sumatoria(1,x) => debe sumar sucesivos numeros 1 
"""
Ej: sumatoria(1,6) => 1+1+1+1+1+1 => 6
sumatoria(1,15) => 1+1+1+1+1+1+1+1+1+1+1+1+1+1+1 => 15
"""
#todo extra: aplicar la misma funcion pero que vaya restando de a 1
#restando(1,15) => 1-1-1-1-1-1-1-1-1-1-1-1-1-1-1 => -13
#restando (1,2) => 1-1 => 0

# homework: buscar en internet ERRORES de python (asserts y exceptions)
"""
ValueError, ZeroDivisionError, IndexError, (cuando intentan convertir una letra a numero)
IndexError: es un error que indica que una busqueda esta fuera de indice

#todo: buscar un caso que pueda generar ese error: 

lista=[1,4,6]
print(lista[6])
"""