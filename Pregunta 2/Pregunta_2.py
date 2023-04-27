"""
El gran almirante del MCU Khan “El Conquistador” es el estratega del multiverso y normalmente se encuentra desbordado de pedidos de 
sugerencia de cómo actuar por las variantes de el mismo de las diferentes épocas y Multiversos. Para lo cual nos solicita desarrollar 
un algoritmo que le permita atender los pedidos de ayuda de acuerdo con la prioridad de los mismo en base a los siguientes 
requerimientos:

se deben contemplar tres niveles de prioridad para la cola;
 
cada pedido de sugerencia cuenta con la siguiente información: nombre del “Khan” solicitante, multiverso en el que se encuentra o el 
más próximo y descripción del pedido;
 
aquellos pedidos que provengan del “Gran Conquistador”, del universo de 616 o la descripción mencione a “El que permanece” tendrán la 
mayor prioridad;
 
si el pedido es del “Khan que todo lo sabe” o la descripción menciona “Carnicero de Dioses” o universo “838” tendrán prioridad media;

el resto de los pedidos serán de prioridad baja;
 
realizar la atención de la cola almacenando los pedidos de mayor prioridad en una pila llamada “bitácora” para revisión y seguimiento;
 
luego de cada atención se podrá agregar un pedido a la cola
"""
from colas import nodoCola, Cola
# La idea principal sera primero almacenar todos los pedidos para luego hacer la atencion
class Pedido(object):
    def __init__(self, nombre, multiverso, descripcion):
        self.nombre = nombre
        self.multiverso = multiverso
        self.descripcion = descripcion
class DatoPedido(object):
    def __init__(self) -> None:
        self.dato = None
    def bitacora(nombre, multiverso, descripcion):
        pedidos = Cola()
        bitacora = Cola()
        # Crearemos la cola de pedidos sin ordenar con un input
        Pedido = input("Teclee 1 si quiere ingresar un pedido:")
        if Pedido == "1":
           nombre = input("NOMBRE >")
           multiverso = input("MULTIVERSO >")
           descripcion = input("DESCRIPCION >")
        else:

        