#eliminar todo, no hace lo mismo que actualizar: eliminar, QUITA el elemento de esa lista:

import verTodo as vt


def eliminarTodo(listado: list):
    vt.verTodo(listado)
    seleccion = int(input("Elija la tarea a eliminar: "))
    elemento = listado.pop(seleccion-1) #pop devuelve lo que eliminamos
    return elemento
    


tareas1= [{'Tarea': 'comprar alimento para el perro', 'Estado': True}, {'Tarea': 'cortar el pasto', 'Estado': False}, {'Tarea': 'hacer la tarea', 'Estado': False}]


