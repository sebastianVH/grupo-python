#condicionales: simples, multiples,anidados


#Operadores logicos

"""

== #igual a: compara que ambos datos sean IDENTICOS en valor y TIPO

"23" -> 23 #son datos distintos
!= #diferentes a: compara ambos datos y se fija que sean DISTINTOS. 

#operadores logicos numericos
>= , <= , > , <

not #el not es para asegurarte que algo no se encuentre
"""
#en este ejercicio, si el usuario tiene 18 o mas años,puede ingresar a nuestro sitio web
"""
edad = int(input("Indiquenos su edad: "))

if edad >= 18:
    print("Usted puede acceder al sitio")
else:
    print("Acceso denegado")
"""


#es un edificio con 8 departamentos,delos cuales 4 estan ocupados.
#depto 1,esta Seba, depto 2 Barbara, depto 3,Julian, depto 4, Messi
#dependiendo el depto que elija el usuario,mostrara el mensaje "Llamando a...*nombre propietario"
#si elige otro numero,mostrara el mensaje "llamando a Porteria"

"""
depto = int(input("¿Con que depto desea comunicarse?: "))

if depto ==1:
    print("LLamando a Seba")
elif depto ==2:
    print("Llamando a Barbara")
elif depto ==3:
    print("Llamando a Julian")
elif depto ==4:
    print("Llamando a Messi")
else:
    print("Llamando a porteria")
"""

#vamos a pedir un numero entero al usuario,y verificar si es multiplo de 2, si es multiplo de 4 (tmb nos diga que es multiplo de 2),o si no es multiplo de 2
"""
numero = int(input("Ingrese un numero ENTERO: "))

if numero % 2 != 0:
    print("No es multiplo de 2")
else:
    if numero % 4 == 0:
        print("Es multiplo de 4 (y ademas de 2)")
    else:
        print("Es multiplo de 2 ")

#match: nos permite,segun la opcion, hacer una comparativa en nuestro programa, y evaluar una condicion ingresada,directamente con los casos disponibles


depto = int(input("¿Con que depto desea comunicarse?: ")) #* con este input, pido el dato del DEPTO que voy a buscar
match depto:
    case 1:
        print("LLamando a Seba")
    case 2:
        print("LLamando a Barbara")
    case 3:
        print("Llamando a Julian")
    case 4:
        print("Llamando a Messi")
    case _: #opcion default (similar a un "else")
        print("Llamando a porteria")



Nuestro programa es de una aerolinea: En nuestro menu, al inicio,lo que pregunta al usuario,
es a que destino desea viajar. Le mostrara en pantalla, las siguientes opciones:

1) Europa
2) Norteamerica
3) Asia

El usuario ingresa un NUMERO de opcion. Segun la opcion,mostrara en pantalla 2 opciones de viaje disponible
por ej,si elige Europa,mostrara Italia, Francia. El usuario elige un destino, y luego el programa pregunta
la cantidad de pasajeros. Luego de que el usuario ingrese la cantidad de pasajeros, le mostrara el importe a 
pagar sino tambien el destino: ej "El total del viaje es de $24000. Espero que disfrute de Francia". 
Cada pasaje tiene un unico precio de $6000.

"""

opcion = int(input("¿A que destino desea viajar?:\n1)Europa\n2)Norteamerica\n3)Asia\n")) #el salto de linea con \n podemos utilzarlo las veces que sean necesarias en una pieza de codigo

if opcion == 1:
    destino=int(input("Elija el destino:\n1)Francia\n2)Italia\n"))
    match destino:
        case 1:
            viaje="Francia"
        case 2:
            viaje="Italia"
elif opcion ==2:
    destino=int(input("Elija el destino:\n1)Miami\n2)New York\n"))
    if destino == 1:
        viaje = "Miami"
    elif destino ==2:
        viaje = "New York"
elif opcion ==3:
    destino=int(input("Elija su destino:\n1)Japon\n2)Rusia\n"))
    if destino ==1:
        viaje = "Japon"
    else:
        viaje ="Rusia"

pasajeros = int(input("Indique la cantidad de pasajeros: "))
total_viaje = 6000*pasajeros

print(f'El total del viaje es de ${total_viaje}. Espero que disfrute de {viaje}.')

