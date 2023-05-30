#from validar import validar
#from consultar import consulta
from extraer import extraccion

"""
El programa tiene 4 opciones: extraccion, deposito, consulta, salir.

Antes de ejecutar el programa principal, debemos validar que el usuario ingrese la contraseña correcta.

#? VALIDADORES TRUE PARA SENTENCIAS 

validador = True # PUEDE TMB VALER FALSE

#al momento de darle un valor a mi validador NO NECESITO COMPARARLO CON OTRA VARIABLE, YA QUE CONTIENE UN VALOR DEL TIPO BOOLEANO
if validador:
    print("El validador es verdadero")
    
SENTENCIAS NO VALIDAS: dan como resultado un False
ej: string vacios (""), numero 0 (dato Integer), booleano False , dato tipo nulo: None

"""
#ingresamos y validamos al usuario
#validar()

#vamos a crear una variable que contenga el saldo del usuario
saldo = 15000

#consulta(saldo)

monto = int(input("Ingrese un monto a extraer: "))
saldo = extraccion(monto,saldo)
print(saldo)

#TODO: crear la funcion de deposito, importarla y usarla
monto = int(input("Ingrese un monto a depositar: "))
saldo = deposito()
print(saldo)