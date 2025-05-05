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
    __slots__ = ("info", "prioridad", "sig")
    def __init__(self, info=None, prioridad=None):
        self.info = info
        self.prioridad = prioridad
        self.sig = None
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
    def atencion(self):
        if self.frente is None:
            return None
        nodo = self.frente
        self.frente = nodo.sig
        if self.frente is None:
            self.final = None
        self.tamaño -= 1
        return nodo.info
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

    def arribo_con_prioridad(self, elemento, prioridad):
        nodo = nodoCola(elemento, prioridad)

        # Caso cola vacía
        if self.frente is None:
            self.frente = self.final = nodo

        # Nueva prioridad es más alta (valor numérico menor) que la del frente
        elif prioridad < self.frente.prioridad:
            nodo.sig = self.frente
            self.frente = nodo

        else:
            ant = self.frente
            # avanzamos hasta encontrar el lugar de inserción
            while ant.sig and ant.sig.prioridad <= prioridad:
                ant = ant.sig
            nodo.sig = ant.sig
            ant.sig = nodo
            # si lo insertamos al final, actualizamos self.final
            if nodo.sig is None:
                self.final = nodo

        self.tamaño += 1

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
def procesa_pedidos(cola, nuevo_pedido, bitacora):
    # Asignar prioridad según reglas
    if (nuevo_pedido.nombre == "Gran Conquistador"
        or nuevo_pedido.multiverso == 616
        or "El que permanece" in nuevo_pedido.descripcion):
        prio = 1
    elif (nuevo_pedido.nombre == "Khan que todo lo sabe"
          or "Carnicero de Dioses" in nuevo_pedido.descripcion
          or nuevo_pedido.multiverso == 838):
        prio = 2
    else:
        prio = 3

    # Insertar en la cola
    cola.arribo_con_prioridad(nuevo_pedido, prio)

    # Atender toda la cola
    while not cola.cola_vacia():
        pedido_atendido = cola.atencion()
        if pedido_atendido.prioridad == 1:
            Pila.apilar(bitacora, pedido_atendido)
        else:
            # Reencolar con su misma prioridad
            cola.arribo_con_prioridad(pedido_atendido, pedido_atendido.prioridad)

    # Mostrar bitácora
    return(Pila.barrido(bitacora))

khan = Pedido("Gran Conquistador", 300, "hola")
Cola_marv = Cola()
bitacora_marv = Pila()
print(procesa_pedidos(Cola_marv, khan, bitacora_marv))

