#IMPORTACION DE FUNCIONES:

def crearLista(num):
    lista = []
    for i in range(num):
        articulo = input("Ingrese articulo: ")
        cantidad = int(input("Ingrese cantidad: "))
        orden = [articulo,cantidad]
        lista.append(orden)
    return lista

def verLista(lista):
    for i in lista:
        print("Articulo a comprar: ",i)