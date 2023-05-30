import crearTodo as ct
import actualizarTodo as at
import verTodo as vt
import eliminarTodo as et

listado_todo = [] #aca almacenamos TODAS NUESTRAS TAREAS

print("Bienvenidos a nuestro programa: ")

while True:
    opciones = int(input("Elija una opcion:\n1)Crear toDo\n2)Actualizar toDo\n3)Ver listado de toDo\n4)Eliminar un toDo\n5)Salir\n>>>"))
    if opciones == 1:
        tarea = input("Ingrese la tarea a realizar: ")
        todo_creado = ct.crearTodo(tarea)
        listado_todo.append(todo_creado)
        print("Tarea agregada con exito")
    elif opciones == 2:
        vt.verTodo(listado_todo)
        completar = int(input("Elija la tarea a completar: "))
        at.actualizarTodo(listado_todo[completar-1])
        