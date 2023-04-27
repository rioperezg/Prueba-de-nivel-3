
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
    def atencion(cola, dato):
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