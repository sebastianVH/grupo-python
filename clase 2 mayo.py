#Bucle for

#? bucle for en recorridos: tenemos un inicio, un final, y una cantidad de PASOS

#* Imprimir los numeros del 1 al 10 con el range():
"""
inicio=1 #indice de inicio de mis iteracciones
fin=21 #cant de iteraciones a realizar partiendo del indice 0
saltos=3 #cant de indices que va a saltar para ejecutar nuevamente el codigo

for i in range(inicio,fin,saltos): # for i in range(1,21,3):
    print("Numero: ",i)
"""
#           0    1    2   3     4    5  6      7    8     9
lista = ["Seba","Juan","Pedro","Marina","Estefi","Julian"]
notas = [10,6,None,9,7,2]


print(len(lista)) #el largo de la lista es un numero entero

"""
for i in range(0,len(lista),2):
    print("Voy a imprimir el indice: ", i)
    print(lista[i])


for i in range(len(lista)):
        print(f"El alumno {lista[i]} tiene de nota {notas[i]}")
        print(f"El alumno {lista[i]} no posee notas")
"""       

#TODO: vamos a crear la lista de compras: llevara un articulo y cantidad a comprar
#? pediremos al usuario, cuantos articulos desea agregar a la lista de compras.  con un recorrido, iremos agregando items a la lista, con sus respectivas cantidades a comprar
"""
cant_art_a_comprar = int(input("¿Cuantos articulos desea agregar a la lista de compras?: "))

lista_compras = []

for i in range(cant_art_a_comprar):
    articulo = input("Ingrese el art a comprar: ")
    cantidad = int(input("Ingrese la cantidad a comprar: "))
    lista_compras.append([articulo,cantidad])
    
print(lista_compras)

"""
#                      0              1            2
#                  0        1       0     1      0       1
lista_compras = [['Harina', 2], ['YErba', 3], ['Azucar', 1]]

for art,cant in lista_compras:
    print(f" De {art} , debo comprar {cant}")
    
    
for i in range(len(lista_compras)): #1
    print(f" De {lista_compras[i][0]}, debo comprar {lista_compras[i][1]}")

