from validar import validar
from consultar import consulta
from extraer import extraccion
from depositar import deposito

#Agregar manejo de Excepciones a lso modulos del programa "cajero"

"""
?---------------LISTA EXCEPCIONES:
! NameError: intento llamar a una variable que NO EXISTE
! IndexError :el emento al cual se intenta acceder esta fuera de rango
! SyntaxError: hay un error en la sintaxis de lo escrito en el codigo!
! KeyError: intentamos acceder a llave inexistente!
! TypeError: Invalida comparaciones u operaciones entre distintos tipos de dato. Ejecutable tmb en parametros de funciones
! ValueError: estoy intentano utilizar una funcion/metodo sobre un valor el cual es imposible convertir
! ImportError /ModuleNotFound: Estamos intentando importar un modulo inexistente o una funcion inexistente
! ZeroDivisionError: Dividir por 0
! UnboundError: Variable que jamas se inicializa (inexistente)

"""

#! funcion validar

contrasenia = [1596,2589,1697,2582]

# a traves de un FOR - IN podria verificar si se encuentra o no, la pass en el listado

#variable para VALIDAR la clave
def validar():
    while True:
        validador = True
        try:
            usuario = int(input("Ingrese su clave de Seguridad: ")) #PODRIA EXISTIR UN ERROR DE TIPO (intentar convertir un caracter a un entero)
        except ValueError:
            print("Se ingresaron caracteres invalidos.")
        else:
            for clave in contrasenia:
                if usuario == clave:
                    print("Bienvenido nuevamente.")
                    validador = False
            if validador:
                print("Clave invalida. Intente Nuevamente.")
            else:
                break
        

#! funcion entraer

def extraccion(monto,saldo):
    while True:
        if monto > saldo:
            print(f"Fondo insuficiente, su saldo es de {saldo}. Ingrese otro importe")
            try:
                print("ultimo monto ingresado:", monto)
                monto = int(input("Ingrese un monto a extraer: "))
            except ValueError:
                print("Se ingresaron caracteres no validos")
        else:
            resto = saldo - monto
            print(f"Se ha retirado {monto} de su cuenta ")
            return resto


#! funcion principal

def progPpal():
    validar()
    saldo = 15000
    while True:
        print()
        try:
            opcion = int(input("Elija la opcion a ejecutar:\n1)Extraccion\n2)Deposito\n3)Consulta\n4)Salir\n>>>")) #conversion
            if opcion == 1:
                monto = int(input("Ingrese un monto a extraer: "))
                saldo = extraccion(monto,saldo)
            elif opcion == 2:
                monto = int(input("Ingrese un monto a depositar: "))
                saldo = deposito(monto,saldo)
            elif opcion == 3:
                consulta(saldo)
            elif opcion == 4:
                print("Gracias por utilizar nuestro servicios.")
                break
            else:
                print("Opcion no valida.")
        except (ValueError, IndexError):
            print("Se han ingresado caracteres no validos")

#? recordemos que TAMBIEN LA EJECUCION  de una funcion/metodo, puede generarnos errores
try:
    progPpal()
except Exception:
    print("Ocurrio un error al ejecutar el programa")

