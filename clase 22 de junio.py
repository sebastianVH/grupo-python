#Creacion de una clase: las clases se crear !!!!CAPITALIZADAS!!!!!

class Automovil():
    #comenzar a definir un estado inicial de mi objeto:
    def __init__(self,marca,modelo,color,fabricacion):
        #estos son los ATRIBUTOS iniciales
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.fabricacion = fabricacion
        #estos atributos hacen referencia a ESTADOS INICIALES que vamos a cambiar
        self.encendido = False #significa que esta apagado
        self.velocidad = 0 #no esta en movimiento o a que velocidad se mueve
        self.acelerar = 0 #me va a generar un movimiento en el auto
        
    #metodo magico __str__ para conocer mas caracteristicas sobre un objeto
    def __str__(self):
        caracteristicas = f'Este auto es un {self.marca}, modelo {self.modelo} del año {self.fabricacion}'
        return caracteristicas
    
    
    
        
mi_auto = Automovil("Ford","Mustang","Verde",1966)
mi_auto2 = Automovil("Chevrolet","Corvette","Blanco",1969)

print(mi_auto)
print(mi_auto2)


"""
Van a crear la clase Persona. Esta clase tiene de atributos iniciales: nombre, edad, nacionalidad , y como estados tiene caminar (estado valor 0), despierto (true)

el metodo str va a devolver lo siguiente: Me llamo *nombre*, tengo *edad* y soy *nacionalidad* => "Me llamo Seba, tengo 36, y soy argentino"

luego instancien 2 personas totalmente distintas. Muestren con un print del objeto, para asegurarse que devuelva de manera correcta el metodo magico con el mensaje que le creamos

"""