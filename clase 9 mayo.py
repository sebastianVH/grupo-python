"""
TODO:
Nuestro programa guardara tareas asignadas por el usuario, las cuales podran luego ser agregadas o quitadas segun al necesidad. 
1) Nos tiene que permitir mostrar LA LISTA DE COSAS A REALIZAR.
2) Nos debe permitir agregar nuevas tareas pendientes.
3) nos tiene que permitir quitar tareas que tengamos realizadas.
4) Nos debe permitir elegir opciones hasta el nosotros decidamos salir.

Nuestras tareas, seran almacenadas en una lista. 

"""

lista_todo = [] #* creamos la lista por fuera, para evitar que nuestro bucle, la vuelva a valor inicial


while True: #*decimos que nuestra condicion es SIEMPRE true ATENCION!!! recordemos usar una sentencia BREAK para salir del bucle
    print("")
    opcion = int(input("Elija una opcion:\n1)Listar TODO's\n2)Agregar Nuevos\n3)Marcar realizadas\n4)Salir\n>>>"))
    if opcion == 1:
        if len(lista_todo) == 0:
            print("Lista Vacia. ")
        else:
            for i in range(len(lista_todo)):
                print(f"{i+1}: {lista_todo[i]}")
                
    elif opcion == 2:
        while True:
            tarea = input("Ingrese la tarea a realizar: ")
            lista_todo.append(tarea)
            print(f" {tarea} fue agregado a la lista de tareas")
            repetir = input("¿Desea cargar otra tarea? S/N: ")
            if repetir == "N" or repetir == 'n':
                break
            
    elif opcion == 3:
        while True:
            if len(lista_todo) == 0:
                print("No hay tareas para eliminar.")
                break
            else:
                for i in range(len(lista_todo)):
                    print(f"{i+1}- {lista_todo[i]}")
                eliminar = int(input("Elija la tarea a eliminar: "))
                tarea_eliminada = lista_todo.pop(eliminar-1)
                print(f"{tarea_eliminada} fue eliminada de la lista.")
                repetir = input("¿Desea eliminar otra tarea? S/N: ")
                if repetir == "N" or repetir == "n":
                    break
    elif opcion == 4:
        print("Gracias por utilizar nuestro programa.")
        break
    else:
        print("Entrada invalida. Por favor, vuelva a elegir una opcion.")
        
        
"""
TODO: en la parte de ELIMINAR UNA TAREA, debe preguntarnos si deseamos eliminar otra. Si ponemos N, salimos, de lo contrario, repetimos el proceso de ELEGIR que tarea quiere eliminar.

"""

