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

class nodoCola(object):
    info, sig = None, None
class Cola(object):
    def __init__(self):
        self.frente, self.final = None, None
        self.tamaño = 0
    def arribo(cola, dato):
        nodo = nodoCola()
        nodo.info = dato
        if cola.frente is None:
            cola.frente = nodo
        else:
            cola.final.sig = nodo
        cola.final = nodo
        cola.tamaño += 1
    def atencion(cola):
        dato = cola.frente.info
        cola.frente = cola.frente.sig
        if cola.frente is None:
            cola.final = None
            cola.tamaño -= 1
        return dato
    def cola_vacia(cola):
        return cola.frente is None
    def en_frente(cola):
        return cola.frente.info
    def tamaño(cola):
        return cola.tamaño
    def mover_al_final(cola):
        dato = Cola.atencion(cola)
        Cola.arribo(cola,dato)
        return dato
    # Primera forma barrido, ineficiente(n^2)
    def barrido(cola):
        caux = Cola()
        while(not Cola.cola_vacia(cola)):
            dato = Cola.atencion(cola)
            print(dato)
            Cola.arribo(caux, dato)
        while(not Cola.cola_vacia(caux)):
            dato = Cola.atencion(caux)
            Cola.arribo(cola,dato)
    # Segunda forma barrido, eficiente(n)
    def barrido2(cola):
        i = 0
        while(i < Cola.tamaño(cola)):
            dato = Cola.mover_al_final(cola)
            print(dato)
            i += 1

    def arribo_con_prioridad(cola, elemento, prioridad):
        nodo = nodoCola()
        nodo.info = elemento
        nodo.prioridad = prioridad
        if cola.frente is None or prioridad < cola.frente.prioridad:
            nodo.sig = cola.frente
            cola.frente = nodo
        else:
            ant = cola.frente
            act = cola.frente.sig
            while(act is not None and act.prioridad <= prioridad):
                ant = act
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        cola.tamaño += 1

class nodoPila(object):
    info, sig = None, None
class Pila(object):
    def __init__(self):
        self.cima = None
        self.tamaño = 0
    def apilar(pila, dato):
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = pila.cima
        pila.tamaño += 1
    def desapilar(pila):
        if pila.cima is None:
           return None  # pila vacía
        x = pila.cima.info      # guardas el valor real
        pila.cima = pila.cima.sig  # mueves la cima al siguiente nodo
        pila.tamaño -= 1
        return x

    def pila_vacia(pila):
        return pila.cima is None
    def en_cima(pila):
        if pila.cima is not None:
            return pila.cima.info
        else:
            return None
    def Tamaño(pila):
        return pila.tamaño
    def barrido(pila):
        paux = Pila()
        while not Pila.pila_vacia(pila):
            dato = Pila.desapilar(pila)
            print(dato)
            Pila.apilar(paux, dato)

        while(Pila.pila_vacia(paux) != None):
            dato = Pila.desapilar(paux)
            Pila.apilar(pila, dato)

class Pedido(object):
    def __init__(self, nombre, multiverso, descripcion):
        self.nombre = nombre
        self.multiverso = multiverso
        self.descripcion = descripcion
        self.prioridad = None
def cola_pedidos(cola, pedido, bitacora):
    if pedido.nombre == "Gran Conquistador" or pedido.multiverso == 616 or pedido.descripcion == "El que permanece":
       pedido.prioridad = 1
       Cola.arribo_con_prioridad(cola, pedido, 1)
    elif pedido.nombre == "Khan que todo lo sabe" or pedido.multiverso == 838 or pedido.descripcion == "Carnicero de Dioses":
        pedido.prioridad = 2
        Cola.arribo_con_prioridad(cola, pedido, 2)
    else:
        pedido.prioridad = 3
        Cola.arribo_con_prioridad(cola, pedido, 3)
    i = Cola.tamaño(cola)
    while i != 0:
        Pedido = Cola.atencion(cola)
        if Pedido.prioridad == 1:
            Pila.apilar(bitacora, Pedido)
        else:
            Cola.arribo_con_prioridad(cola, pedido, pedido.prioridad)
    Cola.barrido(cola)
    Pila.barrido(bitacora)

khan = Pedido("Gran Conquistador", 300, "hola")
Cola_marv = Cola()
bitacora_marv = Pila()
print(cola_pedidos(Cola_marv, khan, bitacora_marv))
