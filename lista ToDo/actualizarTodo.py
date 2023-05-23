#actualizar un todo: va a marcar la tarea como Realizada. Cambia el "Estado" a True
tarea1 = {'Tarea': 'comprar alimento para el perro', 'Estado': False}
tarea2 = {'Tarea': 'cortar el pasto', 'Estado': False}
tarea3 = {'Tarea': 'hacer la tarea', 'Estado': False}

def actualizarTodo(diccionario: dict):
    diccionario["Estado"] = True
    return diccionario
