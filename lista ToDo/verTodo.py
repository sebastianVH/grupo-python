#verTodo: recorre una lista y me muestra cada elemento que hay dentro

def verTodo(listado: list):
    for i in listado:
        if i["Estado"] == True:
            estado = "Completo"
        else:
            estado = "A completar"
        print(f'Tarea: {i["Tarea"]}, Estado: {estado}')
        
        
tareas1= [{'Tarea': 'comprar alimento para el perro', 'Estado': True}, {'Tarea': 'cortar el pasto', 'Estado': False}, {'Tarea': 'hacer la tarea', 'Estado': False}]
